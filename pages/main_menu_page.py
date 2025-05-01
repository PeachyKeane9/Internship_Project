from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from time import sleep

class  MainMenuPage(BasePage):
    #Locators
    SECONDARY_TAB = (By.XPATH, '//a[.//div[@class="g-menu-text" and text()="Secondary"]]')


    def click_secondary_tab(self):
        sleep(5)
        self.wait_and_click(self.SECONDARY_TAB)
