from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    SHOP_CATEGORY = (By.XPATH, "//span[@class='label' and text()='Shop by Category']")
    PRODUCT_CATEGORY_BODY = (By.CSS_SELECTOR, "a.header__menu-item.list-menu__item.focus-inset[href='/collections/body']")

    def open_main_page(self):
        self.driver.get("https://shop.cureskin.com/")

    def click_shop_category(self):
        self.find_element(*self.SHOP_CATEGORY).click()

    def click_body_category(self):
        self.find_element(*self.PRODUCT_CATEGORY_BODY).click()
        sleep(5)



