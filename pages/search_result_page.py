from pages.base_page import Page
from time import sleep


class SearchResult(Page):

    def verify_product_category_result(self, category_name):
        sleep(8)
        self.verify_url_contains_query(category_name)