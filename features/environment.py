from selenium import webdriver
from util import config_util
import allure
from allure import attachment_type

def before_scenario(context, scenario):
    browser = config_util.read_config('basic info', 'browser')
    if browser.__eq__('chrome'):
        context.driver = webdriver.Chrome()
    elif browser.__eq__('firefox'):
        context.driver = webdriver.Firefox()
    elif browser.__eq__('edge'):
        context.driver = webdriver.Edge()
    
    context.driver.maximize_window()
    context.driver.get(config_util.read_config('basic info','url'))

def after_scenario(context, scenario):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='failed_screenshot', attachment_type=attachment_type.PNG)
    
def before_step(context, step):
    pass

