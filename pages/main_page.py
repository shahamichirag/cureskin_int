from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    SHOP_CATEGORY = (By.XPATH, "//span[@class='label' and text()='Shop by Category']")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a.header__menu-item.list-menu__item.focus-inset[href='/collections/{SUBSTR}']")
    SHOP_BUTTON = (By.CSS_SELECTOR, "a.elementor-item[href*='https://shop.cureskin.com']")

    def open_main_page(self):
        self.driver.get("https://shop.cureskin.com/")

    def click_shop_category(self):
        self.find_element(*self.SHOP_CATEGORY).click()

    def get_category(self, category):
        return[self.PRODUCT_CATEGORY[0], self.PRODUCT_CATEGORY[1].replace('{SUBSTR}', category)]

    def click_product_category(self, category):
        locator = self.get_category(category)
        self.wait_for_element_appear(*locator).click()

    





