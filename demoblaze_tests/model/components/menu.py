import allure
from selene.support.shared.jquery_style import s
from selene import have
from demoblaze_tests.data.users import User
from demoblaze_tests.model.components.modal_content import (
    SignUpModal,
    LogInModal,
)


class Menu:
    def __init__(self):
        self.menu = s('#navbarExample').s('.navbar-nav')

        self.sign_up_modal = SignUpModal(s('#signInModal'))
        self.log_in_modal = LogInModal(s('#logInModal'))

    def _select(self, value: str):
        self.menu.ss('.nav-item').element_by(have.text(value)).click()

    @allure.step('Нажать на кнопку \'Home\' в верхнем меню навигации')
    def select_home_tab(self):
        self._select('Home')

    @allure.step('Нажать на кнопку \'Contact\' в верхнем меню навигации')
    def select_contact_tab(self):
        self._select('Contact')

    @allure.step('Нажать на кнопку \'About us\' в верхнем меню навигации')
    def select_about_us_tab(self):
        self._select('About us')

    @allure.step('Нажать на кнопку \'Cart\' в верхнем меню навигации')
    def select_cart_tab(self):
        self.menu.s('#cartur').click()

    @allure.step('Нажать на кнопку \'Log in\' в верхнем меню навигации')
    def select_log_in_tab(self):
        self.menu.s('#login2').click()

    @allure.step('Нажать на кнопку \'Sign up\' в верхнем меню навигации')
    def select_sign_up_tab(self):
        self.menu.s('#signin2').click()

    @allure.step('В верхнем меню навигации отображается: \'Welcome {user}\'')
    def should_have_welcome_phrase(self, user: User):
        self.menu.s('#nameofuser').should(
            have.exact_text(f'Welcome {user.login}')
        )

    @allure.step(
        'В верхнем меню навигации не отображается: \'Welcome {user}\''
    )
    def should_have_no_welcome_phrase(self, user: User):
        s('#nameofuser').should(have.no.exact_text(f'Welcome {user.login}'))
