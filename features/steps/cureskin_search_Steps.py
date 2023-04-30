from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('click on shop by category on main page')
def click_shop_category(context):
    context.app.main_page.click_shop_category()


@when('click on the product category {category}')
def click_product_category(context, category):
    context.app.main_page.click_product_category(category)


@then('verify result for {category_name} category is shown')
def verify_product_category_result(context, category_name):
    context.app.search_result_page.verify_product_category_result(category_name)