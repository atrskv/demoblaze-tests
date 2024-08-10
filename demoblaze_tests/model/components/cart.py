import allure
from selene.support.shared.jquery_style import s
from selene import by, have, be
from demoblaze_tests.data.products import Product


class Cart:
    def __init__(self):
        self.cart = s('#tbodyid')
        self._products = self.cart.ss('tr.success')

    @allure.step('Нажать на кнопку \'Delete\' у \'{value}\'')
    def remove_product(self, value: Product):
        self._products.element_by(have.text(value.name)).s(
            by.link_text('Delete')
        ).click()

    @allure.step('\'{value}\' добавлен в корзину')
    def product_should_be_added(self, value: Product):
        self._products.first.ss('td').second.should(
            have.exact_text(value.name)
        )

    @allure.step('\'{value}\' удален из корзины')
    def product_should_be_removed(self, value: Product):
        self._products.element_by(have.text(value.name)).should(
            be.not_.visible
        )
