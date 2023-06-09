from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
import re
from selenium.webdriver.common.alert import Alert


class ShopFooter(Page):

    EMAIL_FIELD = (By.ID, 'ContactFooter-email')
    SUCCESS_SUBSCRIPTION = (By.CSS_SELECTOR, 'h3#ContactFooter-success')
    EMAIL_SUBMIT_BTN = (By.CSS_SELECTOR, "button[class='button button--arrow field__button animate-arrow']")

    def assert_email_field(self):
        assert self.find_element(*self.EMAIL_FIELD).is_displayed()
        sleep(12)

    def enter_valid_email(self, valid_email):
        self.find_element(*self.EMAIL_FIELD).send_keys(valid_email)
        self.find_element(*self.EMAIL_SUBMIT_BTN).click()

    def successful_subscription(self):
        sleep(24)
        assert self.find_element(*self.SUCCESS_SUBSCRIPTION).is_displayed()

    def enter_invalid_email(self, invalid_email):
        self.find_element(*self.EMAIL_FIELD).send_keys(invalid_email)
        sleep(12)
        self.find_element(*self.EMAIL_SUBMIT_BTN).click()

    def unsuccessful_subscription(self):
        expected_message = 'Please include an @ in the email address'
        alert = Alert(self.driver)
        self.verify_alert_appeared()
        actual_message = alert.text
        assert expected_message in actual_message; \
            f'Expected to see {expected_message} but got {actual_message}'





