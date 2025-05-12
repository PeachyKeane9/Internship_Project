
from selenium.webdriver.common.by import By
from behave import given,when,then
from time import sleep


@when('Log in to the page')
def log_in(context):
    context.app.sign_in_page.log_in()


