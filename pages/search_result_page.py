from pages.base_page import Page


class SearchResult(Page):

    def verify_product_category_result(self, category_name):
        self.verify_url_contains_query(category_name)