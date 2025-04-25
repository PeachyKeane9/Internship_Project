
from selenium.webdriver.common.by import By
from behave import given,when,then
from time import sleep


@when('Log in to the page')
def log_in(context):
    context.app.sign_in_page.log_in()

# @when('Click on the Secondary option at the left side menu')
# pass
#
# @then('Verify the Secondary page opens')
# pass
#
# @when('Advance to final page')
# pass
#
# @when('Retreat to first page')
# pass
