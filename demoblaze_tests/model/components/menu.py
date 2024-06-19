from selene.support.shared.jquery_style import s
from selene import have
from selene.core.entity import Element


class Menu:
    def __init__(self, menu: Element):
        self.menu = menu

    def go_home(self):
        self._select('Home')

    def contact_with_support(self):
        self._select('Contact')

    def check_information_about_company(self):
        self._select('About us')

    def open_cart(self):
        self.menu.s('#cartur').click()

    def log_in(self):
        self.menu.s('#login2').click()

    def sign_up(self):
        self.menu.s('#signin2').click()

    def _select(self, value: str):
        self.menu.ss('.nav-item').element_by(have.text(value)).click()

    @property
    def welcome_phrase(self):
        return s('#nameofuser')
