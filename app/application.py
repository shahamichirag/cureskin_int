from pages.main_page import MainPage
from pages.search_result_page import SearchResult



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResult(self.driver)

