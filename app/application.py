from pages.base_page import BasePage
from pages.main_menu_page import MainMenuPage
from pages.secondary_listings_page import SecondaryListingsPage
from pages.sign_in_page import SignInPage

# from pages.header import Header
# from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.sign_in_page  = SignInPage(driver)
        self.base_page = BasePage(driver)
        self.main_menu_page = MainMenuPage(driver)
        self.secondary_listings_page = SecondaryListingsPage(driver)
        # self.search_results_page = SearchResultsPage(driver)
