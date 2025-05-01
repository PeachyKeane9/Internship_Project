from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from time import sleep

class SignInPage(BasePage):
    #Locators
    EMAIL_FIELD = (By.XPATH, '//div[@class="flex-row-center-2"]//input[@data-name="Email 2"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-name="Password"]')
    LOG_IN_BUTTON = (By.CSS_SELECTOR, 'a[wized="loginButton"]')

    #credientials
    LOG_IN_PAGE_URL = 'https://soft.reelly.io/sign-in'
    EMAIL = 'velot131@gmail.com'
    PASSWORD = 'Mynewpassword!12'

    def log_in(self):
        # Wait for page to load
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.LOG_IN_PAGE_URL))
        sleep(5)


        # Enter email
        email_field = self.find_element(self.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(self.EMAIL)

        # Enter password
        password_field = self.find_element(self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(self.PASSWORD)

        # Click login button
        login_button = self.find_element(self.LOG_IN_BUTTON)
        login_button.click()