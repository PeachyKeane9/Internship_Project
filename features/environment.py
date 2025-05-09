import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # CHROME
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver_path = ChromeDriverManager().install()
    service = ChromeService(driver_path)
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()  # Non-headless: maximize window

    # # # FIREFOX
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    # context.driver.maximize_window()  # Non-headless: maximize window

    # HEADLESS MODE
    #     # CHROME
    # options = ChromeOptions()
    # options.add_argument("headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(driver_path)
    # context.driver = webdriver.Chrome(options=options, service=service)
    # context.driver.set_window_size(1920, 1080)  # Headless: set specific size

        # FIREFOX
    # os.environ["MOZ_HEADLESS"] = "1"  # Only set in headless mode
    # options = FirefoxOptions()
    # options.headless = True
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(options=options, service=service)
    # context.driver.set_window_size(1920, 1080)  # Headless: set specific size
    #
    # # Ensure MOZ_HEADLESS is not set unless explicitly needed
    # if "MOZ_HEADLESS" in os.environ:
    #     os.environ.pop("MOZ_HEADLESS")


## BROWSERSTACK##
    #
    # bs_user ='josephkeane_uvU5JP'
    # bs_key = 'p75kJPb2bRt3Wg7C7yYC'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "10",
    #     'browserName': 'Chrome',
    #
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
    else:
        print("No driver instance to quit. Skipping cleanup.")


