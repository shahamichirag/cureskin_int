from pages.main_page import MainPage
from pages.search_result_page import SearchResult
from pages.shop_page_footer import ShopFooter
from pages.mobile_emulator_Search_page import MobileEmulator



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResult(self.driver)
        self.shop_page_footer = ShopFooter(self.driver)
        self.mobile_emulator_Search_page = MobileEmulator(self.driver)
