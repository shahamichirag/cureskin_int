from pages.base_page import Page


class SearchResult(Page):

    def verify_body_category_result(self):
        self.verify_url_contains_query('body')