import pytest
from demoblaze_tests.data.products import phone
from selene.support.shared.jquery_style import s
from demoblaze_tests.utils import wait_until_alert_is_present
from selene import browser, have


@pytest.fixture
def cart():

    # TODO: IMPLEMENT USING API
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#tbodyid').ss('.card-title').element_by(
        have.exact_text(phone.name)
    ).click()

    s('.product-content').s('.btn-success').click()

    # AND
    wait_until_alert_is_present()
    browser.driver.switch_to.alert.accept()

    s('.navbar-nav').ss('.nav-item').element_by(have.text('Home')).click()

    return phone


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()
