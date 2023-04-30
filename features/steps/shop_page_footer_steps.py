from behave import given, when, then


@when('go to the email field located at the footer of the shop page')
def assert_email_field(context):
    context.app.shop_page_footer.assert_email_field()


@when('enter an invalid email {invalid_email} and hit the submit button')
def enter_invalid_email(context, invalid_email):
    context.app.shop_page_footer.enter_invalid_email(invalid_email)


@when('enter a valid email {valid_email} and hit the submit button')
def enter_valid_email(context, valid_email):
    context.app.shop_page_footer.enter_valid_email(valid_email)


@when('verify successful subscription')
def successful_subscription(context):
    context.app.shop_page_footer.successful_subscription()


@then('verify unsuccessful attempt of subscription')
def unsuccessful_subscription(context):
    context.app.shop_page_footer.unsuccessful_subscription()
