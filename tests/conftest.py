import os
import pytest
from demoblaze_tests.data.products import phone
from demoblaze_tests.data.users import User
from demoblaze_tests.utils import random_string
from dotenv import load_dotenv
from selene.support.shared.jquery_style import s
from demoblaze_tests.utils import wait_until_alert_is_present
from selene import browser, have


@pytest.fixture
def load_env():
    load_dotenv()


@pytest.fixture
def user_with_random_credentials():
    return User(login=random_string(10), password=random_string(10))


@pytest.fixture
def existing_user(load_env):
    return User(login=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))


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
