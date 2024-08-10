import allure
from demoblaze_tests.data.users import User
from demoblaze_tests.model.components.menu import Menu
from selene import be


class Account:
    def __init__(self):
        self.menu = Menu()

    @allure.step('Зарегистрироваться')
    def sign_up(self, user: User):
        self.menu.select_sign_up_tab()
        self.menu.sign_up_modal.fill(user.login, user.password)
        self.menu.sign_up_modal.confirm()

    @allure.step('Авторизоваться')
    def log_in(self, user: User):
        self.menu.select_log_in_tab()
        self.menu.log_in_modal.fill(user.login, user.password)
        self.menu.log_in_modal.confirm()

    @allure.step('Пользователь зарегистрирован')
    def user_should_be_signed_up(self):
        self.menu.sign_up_modal.alert.should_have_exact_text(
            'Sign up successful.'
        )
        self.menu.sign_up_modal.alert.accept()

        self.menu.sign_up_modal.data.should(be.not_.visible)

    @allure.step('Пользователь авторизован')
    def should_be_logged_in(self, user: User):
        self.menu.sign_up_modal.data.should(be.not_.visible)
        self.menu.should_have_welcome_phrase(user)

    @allure.step('Пользователь не авторизован')
    def should_be_not_logged_in(self, user: User):
        self.menu.sign_up_modal.alert.should_have_exact_text('Wrong password.')
        self.menu.sign_up_modal.alert.accept()

        self.menu.sign_up_modal.data.should(be.not_.visible)
        self.menu.should_have_no_welcome_phrase(user)
