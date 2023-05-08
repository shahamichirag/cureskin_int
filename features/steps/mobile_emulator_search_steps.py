from behave import given, when, then


@given('Click the main menu')
def click_main_menu(context):
    context.app.mobile_emulator_Search_page.click_main_menu()


@when('click on shop icon on main menu shown on the mobile screen')
def click_shop_icon_from_menu(context):
    context.app.mobile_emulator_Search_page.click_shop_icon_from_menu()


@when('click on the product body category on mobile screen')
def click_product_category_mobile_screen(context):
    context.app.mobile_emulator_Search_page.click_product_category_mobile_screen()


@then('verify result for body category is shown on mobile screen')
def verify_result_shown_mobile(context):
    context.app.mobile_emulator_Search_page.verify_result_shown_mobile()