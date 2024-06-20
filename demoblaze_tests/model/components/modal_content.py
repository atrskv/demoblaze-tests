from selene.core.entity import Element
from demoblaze_tests.utils import wait_until_alert_is_present
from selene import browser
from selene.support.shared.jquery_style import s


class Alert:

    def confirm(self):
        wait_until_alert_is_present()
        browser.driver.switch_to.alert.accept()


class Notification:
    def __init__(self):
        self.notification = s('.sweet-alert')

    @property
    def title(self):
        return self.notification.s('h2')


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


class OrderModal(Modal):
    def __init__(self, modal: Element):
        super().__init__(modal)
        self.notification = Notification()

    def fill(
        self,
        name: str,
        country: str,
        city: str,
        credit_card: str,
        month,
        year: str,
    ):
        self._modal.s('#name').type(name)
        self._modal.s('#country').type(country)
        self._modal.s('#city').type(city)
        self._modal.s('#card').type(credit_card)
        self._modal.s('#month').type(month)
        self._modal.s('#year').type(year)
