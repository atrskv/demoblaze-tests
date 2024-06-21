import allure
from selene.support.shared.jquery_style import s
from selene import by, have, be


class Cart:
    def __init__(self):
        self.cart = s('#tbodyid')
        self._products = self.cart.ss('tr.success')

    @allure.step('Нажать на кнопку "Delete" у {value}')
    def remove_product(self, value: str):
        self._products.element_by(have.text(value)).s(
            by.link_text('Delete')
        ).click()

    @property
    def name_of_added_product(self):
        return self._products.first.ss('td').second

    @allure.step('{value} добавлен в корзину')
    def product_should_be_added(self, value: str):
        self._products.first.ss('td').second.should(have.exact_text(value))

    @allure.step('{value} удален из корзины')
    def product_should_be_removed(self, value: str):
        self._products.element_by(have.text(value)).should(be.not_.visible)
