from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('click on shop by category on main page')
def click_shop_category(context):
    context.app.main_page.click_shop_category()


@when('click on the product category "body"')
def click_body_category(context):
    context.app.main_page.click_body_category()


@then('verify result for "body" category is shown')
def verify_body_category_result(context):
    context.app.search_result_page.verify_body_category_result()