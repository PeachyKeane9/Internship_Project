from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SecondaryListingsPage(BasePage):
    #Locators
    SEC_HEADER_TAB = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43")
    PARTIAL_URL = 'secondary-listings'

    PREVIOUS_PAGE_BTN = (By.CSS_SELECTOR, 'div[wized="previousPageMLS"]')
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')
    FIRST_LISTING_CARD = (By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')



    def verify_secondary_list_pg(self):
     # self.wait_for_element_appear(self. SEC_HEADER_TAB)
     self.verify_partial_url(self.PARTIAL_URL)

    def advance_final_page(self):
        for _ in range(135):
            # self.wait_for_element_appear(self.FIRST_LISTING_CARD)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.FIRST_LISTING_CARD)
            )
            # self.scroll_and_click(self.FIRST_LISTING_CARD, timeout=20)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next_button = self.wait_for_element_appear(self.NEXT_PAGE_BTN)
            if 'disabled' in next_button.get_attribute('class') or not next_button.is_enabled():
                print("Last page has been reached")
                break
            self.wait_and_click(self.NEXT_PAGE_BTN)
            sleep(5)

    def retreat_first_page(self):
        for _ in range(134):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait_for_element_appear(self.FIRST_LISTING_CARD)
            prev_button = self.wait_for_element_appear(self.PREVIOUS_PAGE_BTN )
            if 'disabled' in prev_button.get_attribute('class') or not prev_button.is_enabled():
                print("Returned to the first page.Pagination buttons function. ")
                break
            self.wait_and_click(self.PREVIOUS_PAGE_BTN )