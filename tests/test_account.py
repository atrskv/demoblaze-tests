from selene import browser, be, have
from selene.support.shared.jquery_style import s
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from demoblaze_tests.utils import wait_until_alert_is_present


def test_register_an_user_successfully(
    user_with_random_credentials,
):

    # GIVEN
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#signin2').click()
    s('#sign-username').type(user_with_random_credentials.login)
    s('#sign-password').type(user_with_random_credentials.password)
    s('#signInModal').s('.btn-primary').click()

    # AND
    wait_until_alert_is_present()
    browser.driver.switch_to.alert.accept()

    # THEN
    s('#signInModal').should(be.not_.visible)


def test_authorize_an_existing_user(existing_user):

    # GIVEN
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#login2').click()
    s('#loginusername').type(existing_user.login)
    s('#loginpassword').type(existing_user.password)
    s('#logInModal').s('.btn-primary').click()

    # THEN
    s('#nameofuser').should(have.exact_text(f'Welcome {existing_user.login}'))


def test_register_an_user_unsuccessfully(existing_user):

    # GIVEN
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#login2').click()
    s('#loginusername').type(existing_user.login)
    s('#loginpassword').type(existing_user.login)
    s('#logInModal').s('.btn-primary').click()

    # AND
    wait = WebDriverWait(browser.driver, 4)
    wait.until(expected_conditions.alert_is_present())

    browser.driver.switch_to.alert.accept()

    # THEN
    s('#logInModal').s('.close').click()
    s('#nameofuser').should(be.hidden)
