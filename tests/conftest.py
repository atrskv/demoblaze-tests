import pytest
import settings
from selene import browser
from selenium.webdriver.chrome.options import Options
from demoblaze_tests.model.client import ApiClient
from demoblaze_tests.utils import (
    add_browser_logs,
    add_screenshot,
    add_html,
    add_video,
)
import allure
from demoblaze_tests.data import users, products


@pytest.fixture(scope='function', autouse=True)
def given_browser_management():

    browser.config.window_width = settings.config.window_width
    browser.config.window_height = settings.config.window_height
    browser.config.base_url = settings.config.base_url
    browser.config.timeout = settings.config.timeout

    with allure.step('Начать сессию'):
        if settings.config.context == 'local':

            browser.config.driver_name = settings.config.driver_name

        if settings.config.context == 'remote':

            selenoid_capabilities = {
                'browserName': settings.config.driver_name,
                'browserVersion': settings.config.driver_version,
                'selenoid:options': {'enableVNC': True, 'enableVideo': True},
            }

            options = Options()
            options.capabilities.update(selenoid_capabilities)

            selenoid_login = settings.config.selenoid_login
            selenoid_pass = settings.config.selenoid_pass
            selenoid_url = settings.config.selenoid_url

            browser.config.driver_remote_url = f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub'

            browser.config.driver_options = options

    yield

    with allure.step('Завершить сессию'):
        add_screenshot()

        # For more details: https://github.com/SeleniumHQ/selenium/issues/1161
        if not settings.config.driver_name == 'firefox':
            add_browser_logs()

        add_html()

        if settings.config.context == 'remote':
            add_video()

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
@allure.step('Товары получены')
def given_products():
    return products.catalog


@pytest.fixture(scope='session', autouse=False)
@allure.step('API клиент инициализирован')
def given_api_client():
    return ApiClient()


@pytest.fixture(scope='function', autouse=False)
@allure.step('Пользователь сгенерирован')
def given_generated_user():
    return users.generate()


@pytest.fixture(scope='function', autouse=False)
@allure.step('Пользователь зарегистрирован')
def given_existing_user(given_generated_user, given_api_client):

    user = given_generated_user
    api = given_api_client

    api.sign_up(user)

    return user


@pytest.fixture(scope='function', autouse=False)
@allure.step('Товары добавлены в корзину')
def given_cart_with_products(given_api_client):
    _products = products.catalog.by_names(
        'Nokia lumia 1520', 'Sony vaio i5', 'Iphone 6 32gb'
    )
    api = given_api_client
    api.add_products_to_cart(*_products)

    return _products
