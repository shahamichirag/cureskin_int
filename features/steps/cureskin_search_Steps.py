from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('click on "shop by category"')
def click_shop_category(context):
    context.app.click_shop_category()


@when('click on "Body"')
def click_body_category(context):
    context.app.main_page.click_body_category()


@then('verify "Body" header is shown')
def verify_body_category_result(context):
    context.app.main_page.verify_body_category_result()