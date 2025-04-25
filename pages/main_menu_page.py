from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from time import sleep

class  MainMenuPage(BasePage):
    #Locators
    SECONDARY_TAB = (By.ID, "w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b")

    def click_secondary_tab(self):
        self.wait_and_click(self.SECONDARY_TAB)
