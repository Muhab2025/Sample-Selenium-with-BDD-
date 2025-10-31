from behave import *
from features.pages.homepage import HomePage
from util import baseutil

@given(u'I navigate to Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.login_page = context.home_page.navigate_to_login_page()

@when(u'I enter a valid username as "{email}" and a valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)

@when(u'I click on Login button')
def step_impl(context):
    context.my_account_page = context.login_page.click_login_btn()

@then(u'I should get logged in my account page')
def step_impl(context):
    assert context.my_account_page.display_edit_your_account_message()

@when(u'I enter an invalid username and a valid password as "{valid_password}" into the fields')
def step_impl(context, valid_password):
    context.login_page.enter_email_address(baseutil.generate_email_with_timestamp())
    context.login_page.enter_password(valid_password)

@when(u'I enter a valid username as "{valid_email}" and an invalid password as "{invalid_password}" into the fields')
def step_impl(context, valid_email, invalid_password):
    context.login_page.enter_email_address(valid_email)
    context.login_page.enter_password(invalid_password)

@when(u'I enter an invalid username and an invalid password as "{invalid_password}" into the fields')
def step_impl(context, invalid_password):
    context.login_page.enter_email_address(baseutil.generate_email_with_timestamp())
    context.login_page.enter_password(invalid_password)

@when(u'I do not enter any credentials into the fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

@then(u'I should get an appropriate warning message')
def step_impl(context):
    assert context.login_page.display_invalid_credentials_message()
 