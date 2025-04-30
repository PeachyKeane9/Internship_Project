import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # CHROME
    # options = webdriver.ChromeOptions()
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(driver_path, log_path="chromedriver.log")
    # context.driver = webdriver.Chrome(service=service, options=options)

    # FIREFOX
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # HEADLESS MODE
        # CHROME
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # service = ChromeService(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

        # FIREFOX
    # Set environment variable to enforce headless mode
    os.environ["MOZ_HEADLESS"] = "1"  # Tell Firefox to run in headless mode

    options = webdriver.FirefoxOptions()
    options.headless = True  # Set headless property
    options.add_argument("--headless")  # Also add the argument for redundancy
    options.add_argument("--disable-gpu")  # Stability option
    options.add_argument("--no-sandbox")  # Stability option
    driver_path = GeckoDriverManager().install()
    service = FirefoxService(driver_path, log_path="geckodriver.log")
    context.driver = webdriver.Firefox(
        options=options,
        service=service
    )

    # Use set_window_size for headless mode
    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)

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