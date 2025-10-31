from behave import *
from util import baseutil
from pages.homepage import HomePage


@given('I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.register_page = context.home_page.navigate_to_registration_page()

@when(u'I enter below data in all mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.register_account(row['first_name'], row['last_name'], baseutil.generate_email_with_timestamp(), \
            row['telephone'], row['password'], row['password'], 'No', 'yes')

@when(u'I click on Continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_continue()

@when(u'I enter below data in all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.register_account(row['first_name'], row['last_name'], baseutil.generate_email_with_timestamp(), \
            row['telephone'], row['password'], row['password'], 'yes', 'yes')

@when(u'I enter an existing email address')
def step_impl(context):
    for row in context.table:
        context.register_page.register_account(row['first_name'], row['last_name'], row['e-mail'], row['telephone'], \
            row['password'], row['password'], 'No', 'yes')

@when(u'I do not enter any data in the fields')
def step_impl(context):
    context.register_page.register_account('', '', '', '', '', '', 'No', 'No')

@then(u'I should be redirected to Account Success Page')
def step_impl(context):
    assert context.account_success_page.display_account_created_message()

@then(u'Appropriate warning message should be displayed')
def step_impl(context):
    assert context.register_page.display_duplicate_email_warning_message()

@then(u'Appropriate warning messages should be displayed')
def step_impl(context):
    assert context.register_page.display_all_warning_messages()


