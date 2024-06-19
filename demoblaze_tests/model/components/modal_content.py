from selene.core.entity import Element
from demoblaze_tests.utils import wait_until_alert_is_present
from selene import browser


class Alert:

    def confirm(self):
        wait_until_alert_is_present()
        browser.driver.switch_to.alert.accept()


class Modal:
    def __init__(self, modal: Element):
        self._modal = modal
        self._alert = Alert()

    def confirm(self):
        self._modal.s('.btn-primary').click()

    def cancel(self):
        self._modal.s('.btn-secondary').click()

    def close(self):
        self._modal.s('.close').click()

    @property
    def user_data(self):
        return self._modal

    @property
    def alert(self):
        return self._alert


class SignUpModal(Modal):

    def fill(self, username: str, password: str):
        self._modal.s('#sign-username').type(username)
        self._modal.s('#sign-password').type(password)


class LogInModal(Modal):

    def fill(self, username: str, password: str):
        self._modal.s('#loginusername').type(username)
        self._modal.s('#loginpassword').type(password)
