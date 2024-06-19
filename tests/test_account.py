from selene import browser, be, have
from selene.support.shared.jquery_style import s
from demoblaze_tests.utils import wait_until_alert_is_present
from demoblaze_tests.data import users


def test_register_an_user_successfully():

    # GIVEN
    user = users.user_with_random_credentials
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#signin2').click()
    s('#sign-username').type(user.login)
    s('#sign-password').type(user.password)
    s('#signInModal').s('.btn-primary').click()

    # AND
    wait_until_alert_is_present()
    browser.driver.switch_to.alert.accept()

    # THEN
    s('#signInModal').should(be.not_.visible)


def test_authorize_an_existing_user():

    # GIVEN
    user = users.existing_user
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#login2').click()
    s('#loginusername').type(user.login)
    s('#loginpassword').type(user.password)
    s('#logInModal').s('.btn-primary').click()

    # THEN
    s('#nameofuser').should(have.exact_text(f'Welcome {user.login}'))


def test_register_an_user_unsuccessfully():

    # GIVEN
    user = users.existing_user
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#login2').click()
    s('#loginusername').type(user.login)
    s('#loginpassword').type(user.login)
    s('#logInModal').s('.btn-primary').click()

    # AND
    wait_until_alert_is_present()
    browser.driver.switch_to.alert.accept()

    # THEN
    s('#logInModal').s('.close').click()
    s('#nameofuser').should(be.hidden)
