from demoblaze_tests.app import app
from allure_commons.types import Severity
from demoblaze_tests.utils import allure


@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Регистрация нового пользователя')
def test_sign_up_a_new_user_successfully(given_generated_user):

    user = given_generated_user

    app.home_page.open()
    app.home_page.account.sign_up(user)

    app.home_page.account.user_should_be_signed_up()


@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Авторизация существующего пользователя')
def test_log_in_using_an_existing_user_account(given_existing_user):

    user = given_existing_user

    app.home_page.open()
    app.home_page.account.log_in(user)

    app.home_page.account.should_be_logged_in(user)


@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Авторизация существующего пользователя с неправильным паролем')
def test_log_in_using_an_existing_user_account_with_wrong_password(
    given_existing_user,
):

    user = given_existing_user
    user.password = 'wrong'

    app.home_page.open()
    app.home_page.account.log_in(user)

    app.home_page.account.should_be_not_logged_in(user)
