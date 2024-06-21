import allure
from selene.core.entity import Element
from demoblaze_tests.utils import wait_until_alert_is_present
from selene import browser, have
from selene.support.shared.jquery_style import s


class Alert:

    @allure.step('Подтвердить действие в предупреждении ')
    def confirm(self):
        wait_until_alert_is_present()
        browser.driver.switch_to.alert.accept()


class Notification:
    def __init__(self):
        self.notification = s('.sweet-alert')

    @allure.step(
        'Заказ оформлен, пользователь видит уведомление: "Thank you for your purchase!"'
    )
    def should_have_successful_message(self):
        self.notification.s('h2').should(
            have.exact_text('Thank you for your purchase!')
        )


class Modal:
    def __init__(self, modal: Element):
        self._modal = modal
        self._alert = Alert()

    @allure.step('Подтвердить действие в модальном окне')
    def confirm(self):
        self._modal.s('.btn-primary').click()

    @allure.step('Отменить действие в модальном окне')
    def cancel(self):
        self._modal.s('.btn-secondary').click()

    @allure.step('Закрыть модальное окно')
    def close(self):
        self._modal.s('.close').click()

    @property
    def alert(self):
        return self._alert

    @allure.step('Пользователь зарегистрирован, модальное окно закрыто')
    def user_data_should_be_not_visible(self):
        return self._modal


class SignUpModal(Modal):

    @allure.step(
        'В модальном окне заполнить текстовое поле "Username" и "Password"'
    )
    def fill(self, username: str, password: str):
        self._modal.s('#sign-username').type(username)
        self._modal.s('#sign-password').type(password)


class LogInModal(Modal):

    @allure.step(
        'В модальном окне заполнить текстовое поле "Username" и "Password"'
    )
    def fill(self, username: str, password: str):
        self._modal.s('#loginusername').type(username)
        self._modal.s('#loginpassword').type(password)


class OrderModal(Modal):
    def __init__(self, modal: Element):
        super().__init__(modal)
        self.notification = Notification()

    @allure.step(
        'В модальном окне заполнить текстовые поля: "Name", "Country", "City", "Credit card", "Month", "Year"'
    )
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
