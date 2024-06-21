from demoblaze_tests.data import users
from demoblaze_tests.app import app
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Регистрация нового пользователя')
def test_register_an_user_successfully():

    user = users.user_with_random_credentials

    app.home_page.open()
    app.home_page.menu.sign_up()
    app.home_page.sign_up_modal.fill(user.login, user.password)
    app.home_page.sign_up_modal.confirm()
    app.home_page.sign_up_modal.alert.confirm()

    app.home_page.sign_up_modal.user_data_should_be_not_visible()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Авторизация существующего пользователя')
def test_log_in_using_an_existing_user_account():

    user = users.existing_user

    app.home_page.open()
    app.home_page.menu.log_in()
    app.home_page.log_in_modal.fill(user.login, user.password)
    app.home_page.log_in_modal.confirm()

    app.home_page.menu.welcome_phrase_should_have_exact_text(user.login)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Авторизация существующего пользователя с неверным паролем')
def test_log_in_unsuccessfully():

    user = users.existing_user

    app.home_page.open()
    app.home_page.menu.log_in()
    app.home_page.log_in_modal.fill(user.login, password='invalid password')
    app.home_page.log_in_modal.confirm()
    app.home_page.log_in_modal.alert.confirm()
    app.home_page.log_in_modal.close()

    app.home_page.menu.welcome_phrase_should_be_not_visible()
