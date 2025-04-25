from selenium.webdriver.common.by import By
from behave import given,when,then
from time import sleep

@given('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io')

@when('Click on the Secondary option at the left side menu')
def click_secondary_tab(context):
    context.app.main_menu_page.click_secondary_tab()
