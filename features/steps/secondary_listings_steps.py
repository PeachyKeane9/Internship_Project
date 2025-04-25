
from selenium.webdriver.common.by import By
from behave import given,when,then
from time import sleep


@then('Verify the Secondary page opens')
def verify_secondary_list_pg(context):
    context.app.secondary_listings_page.verify_secondary_list_pg()

@when('Advance to final page')
def advance_final_page(context):
    context.app.secondary_listings_page.advance_final_page()



@when('Retreat to first page')
def retreat_first_page(context):
    context.app.secondary_listings_page.retreat_first_page()