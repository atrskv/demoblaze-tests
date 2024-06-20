import pytest
from selene import browser

from demoblaze_tests.utils import add_logs, add_screenshot, add_html


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://www.demoblaze.com'

    yield

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)

    browser.quit()
