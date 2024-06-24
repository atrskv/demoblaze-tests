import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options

from demoblaze_tests.app import app
from demoblaze_tests.utils import (
    add_logs,
    add_screenshot,
    add_html,
    add_video,
)
from dotenv import load_dotenv
import os


def configure_browser(options):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://www.demoblaze.com'
    browser.config.driver_options = options


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_management_remote():

    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'selenoid:options': {'enableVNC': True, 'enableVideo': True},
    }

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_pass = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv('SELENOID_URL')

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver_remote_url = (
        f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub'
    )

    configure_browser(options)

    yield

    add_screenshot()
    add_logs()
    add_html()
    add_video()

    browser.quit()


@pytest.fixture(scope='function')
def browser_management_local():
    options = Options()
    configure_browser(options)

    yield

    add_screenshot()
    add_logs()
    add_html()

    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--mode',
        action='store',
        default='local',
        help='Запуск локально/удаленно',
    )


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    mode = request.config.getoption('--mode')
    if mode == 'remote':
        request.getfixturevalue('browser_management_remote')
    else:
        request.getfixturevalue('browser_management_local')


@pytest.fixture(scope='function')
def log_in():
    def _log_in(username, password):
        app.home_page.menu.select_log_in()
        app.home_page.log_in_modal.fill(username, password)
        app.home_page.log_in_modal.confirm()

    return _log_in
