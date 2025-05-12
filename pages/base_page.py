from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

from support.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait  = WebDriverWait(self.driver,15)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator{locator} not clickable'
        ).click()

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in {actual_url}'

    def wait_for_element_appear(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} did not appear')

    def scroll_and_click(self, locator, timeout=10, retries=2):
        attempt = 0
        while attempt < retries:
            try:
                wait = WebDriverWait(self.driver, timeout)

                element = wait.until(EC.presence_of_element_located(locator))
                wait.until(EC.visibility_of(element))
                element = wait.until(EC.element_to_be_clickable(locator))

                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                ActionChains(self.driver).move_to_element(element).perform()
                element.click()
                return  # success — exit the method

            except StaleElementReferenceException as e:
                print(f"StaleElementReferenceException on attempt {attempt + 1}, retrying...")
                attempt += 1
                if attempt == retries:
                    self.driver.save_screenshot("scroll_and_click_stale_element.png")
                    with open("page_source_stale.html", "w") as f:
                        f.write(self.driver.page_source)
                    raise Exception(f"Element became stale after {retries} retries: {str(e)}")

            except TimeoutException as e:
                self.driver.save_screenshot("scroll_and_click_timeout.png")
                with open("page_source_timeout.html", "w") as f:
                    f.write(self.driver.page_source)
                raise TimeoutException(
                    f"Element by {locator[0]}='{locator[1]}' not clickable after {timeout} seconds: {str(e)}"
                )

    def is_mobile(self):
        """Detect if the test is running in mobile emulation by checking the user agent."""
        user_agent = self.driver.execute_script("return navigator.userAgent;")
        is_mobile = "Mobile" in user_agent or "iPhone" in user_agent
        print(f"User Agent: {user_agent}, Is Mobile: {is_mobile}")  # Debugging
        return is_mobile
