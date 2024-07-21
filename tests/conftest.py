import pytest
import config
from selene import browser
from selenium.webdriver.chrome.options import Options
from demoblaze_tests.utils import (
    add_logs,
    add_screenshot,
    add_html,
    add_video,
)


def configure_browser():
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.base_url = config.base_url


@pytest.fixture(scope='function')
def local_browser():

    configure_browser()

    yield

    add_screenshot()
    add_logs()
    add_html()

    browser.quit()


@pytest.fixture(scope='function')
def remote_browser():

    selenoid_capabilities = {
        'browserName': 'chrome',
        'selenoid:options': {'enableVNC': True, 'enableVideo': True},
    }

    options = Options()
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = config.selenoid_login
    selenoid_pass = config.selenoid_pass
    selenoid_url = config.selenoid_url

    browser.config.driver_remote_url = (
        f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub'
    )

    browser.config.driver_options = options

    configure_browser()

    yield

    add_screenshot()
    add_logs()
    add_html()
    add_video()

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    if config.context == 'local':
        request.getfixturevalue('local_browser')
    if config.context == 'remote':
        request.getfixturevalue('remote_browser')
    ...
