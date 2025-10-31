from behave import *
from features.pages.homepage import HomePage

@given('I am on the Application Homepage')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.verify_page_title('https://tutorialsninja.com/demo/', 'Your Store')

@when('I enter a valid product say "{valid_product}" into search box field')
def step_impl(context, valid_product):
    context.home_page.enter_product_into_search_box_field(valid_product)

@when('I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_search_button()

@then('Valid products should be displayed on search results page')
def step_impl(context):
    assert context.search_page.display_status_of_valid_product()

@when(u'I enter an invalid product say "{invalid_product}" into search box field')
def step_impl(context, invalid_product):
    context.home_page.enter_product_into_search_box_field(invalid_product)

@when(u'I do not enter any product into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")

@then(u'Appropriate message should be displayed on search results page')
def step_impl(context):
    assert context.search_page.display_invalid_product_message()
