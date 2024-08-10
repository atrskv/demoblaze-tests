import allure
from demoblaze_tests.model.components.account import Account
from demoblaze_tests.model.components.menu import Menu
from selene.support.shared.jquery_style import s
from selene import browser
from demoblaze_tests.model.components.products import (
    Products,
)


class HomePage:
    def __init__(self):
        self.products = Products(s('#tbodyid'))
        self.menu = Menu()
        self.account = Account()

    @allure.step('Открыть стартовую страницу сайта')
    def open(self):
        browser.open('/')
