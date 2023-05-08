from pages.base_page import Page
from selenium.webdriver.common.by import By


class MobileEmulator(Page):

    MAIN_MENU = (By.CSS_SELECTOR, "div.elementor-image a[href*='#elementor-action']")
    SHOP_ICON = (By.CSS_SELECTOR, "ul#menu-1-68391f2 a[href*='https://shop.cureskin.com']")
    SHOP_BY_CATEGORY_MENU = (By.CSS_SELECTOR, '.menu-drawer-container')
    PRODUCT_CATEGORY = (By.XPATH,
                        "//span[contains(@class,'menu-drawer__menu-item list-menu__item') and text()='Shop by Category'] ")
    CATEGORY_RESULT = (By.CSS_SELECTOR, "a[href='/collections/body']")
    BODY_PRODUCT = (By.CSS_SELECTOR, "a.card-information__text.h4[href*='/collections/body/products/']")

    def click_main_menu(self):
        self.find_element(*self.MAIN_MENU).click()

    def click_shop_icon_from_menu(self):
        self.find_element(*self.SHOP_ICON).click()

    def click_product_category_mobile_screen(self):
        self.find_element(*self.SHOP_BY_CATEGORY_MENU).click()
        self.find_element(*self.PRODUCT_CATEGORY).click()
        self.find_element(*self.CATEGORY_RESULT).click()

    def verify_result_shown_mobile(self):
        assert self.find_element(*self.BODY_PRODUCT).is_displayed()




