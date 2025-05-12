from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from time import sleep


class MainMenuPage(BasePage):
    # locators
    OFF_PLAN_WEB = (By.XPATH, "//a[@wized='newOffPlanLink']//div[@class='g-menu-text' and text()='Off-plan']")
    SECONDARY_TAB_WEB = (By.XPATH, "//a[contains(@href, 'secondary-listings')]//button[contains(text(), 'Secondary')]")

    # Mobile locators
    OFF_PLAN_MOBILE = (By.XPATH, "//a[contains(@class, 'menu-link') and .//div[contains(text(), 'Off-plan')]]")

    SECONDARY_TAB_MOBILE = (By.CSS_SELECTOR, "button.pb-5.text-sm.font-semibold.border-b-2.text-muted-foreground")




    def click_secondary_tab(self):
        # Step 1: Wait for OFF_PLAN to be present and click it
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.OFF_PLAN_MOBILE)
        )
        self.scroll_and_click(self.OFF_PLAN_MOBILE, timeout=20)

        # Step 2: Wait for SECONDARY_TAB to become visible and click it
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SECONDARY_TAB_MOBILE)
        )
        self.wait_and_click(self.SECONDARY_TAB_MOBILE)

