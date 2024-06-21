import allure
from selene.support.shared.jquery_style import s
from selene import have, be


class Menu:
    def __init__(self):
        self.menu = s('#navbarExample').s('.navbar-nav')

    @allure.step('Нажать на кнопку "Home" в верхнем меню навигации')
    def go_home(self):
        self._select('Home')

    @allure.step('Нажать на кнопку "Contact" в верхнем меню навигации')
    def contact_with_support(self):
        self._select('Contact')

    @allure.step('Нажать на кнопку "About us" в верхнем меню навигации')
    def check_information_about_company(self):
        self._select('About us')

    @allure.step('Нажать на кнопку "Cart" в верхнем меню навигации')
    def open_cart(self):
        self.menu.s('#cartur').click()

    @allure.step('Нажать на кнопку "Log in" в верхнем меню навигации')
    def log_in(self):
        self.menu.s('#login2').click()

    @allure.step('Нажать на кнопку "Sing up" в верхнем меню навигации')
    def sign_up(self):
        self.menu.s('#signin2').click()

    def _select(self, value: str):
        self.menu.ss('.nav-item').element_by(have.text(value)).click()

    @allure.step(
        'Пользователь авторизован, в верхнем меню навигации отображается: "Welcome {value}"'
    )
    def welcome_phrase_should_have_exact_text(self, value: str):
        s('#nameofuser').should(have.exact_text(f'Welcome {value}'))

    @allure.step(
        'Пользователь не авторизован, в верхнем меню навигации не отображается: "Welcome <username>"'
    )
    def welcome_phrase_should_be_not_visible(self):
        s('#nameofuser').should(be.not_.visible)
