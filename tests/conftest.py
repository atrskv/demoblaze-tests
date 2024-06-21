import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from demoblaze_tests.utils import (
    add_logs,
    add_screenshot,
    add_html,
    add_video,
)
from dotenv import load_dotenv
import os


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://www.demoblaze.com'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver_remote_url = (
        f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
    )

    browser.config.driver_options = options

    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()
