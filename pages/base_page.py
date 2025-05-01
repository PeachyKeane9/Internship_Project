from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
