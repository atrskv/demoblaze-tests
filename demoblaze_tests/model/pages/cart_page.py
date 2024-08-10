import allure
from demoblaze_tests.data.users import User
from demoblaze_tests.model.components.cart import Cart
from demoblaze_tests.model.components.menu import Menu
from demoblaze_tests.model.components.modal_content import (
    OrderModal,
)
from selene.support.shared.jquery_style import s
from selene import browser


class CartPage:
    def __init__(self):
        self.menu = Menu()
        self.cart = Cart()
        self.order_modal = OrderModal(s('#orderModal'))

    @allure.step('Открыть корзину')
    def open(self):
        browser.open('/cart.html')

    @allure.step('Нажать на кнопку \'Place Order\'')
    def click_place_order_button(self):
        s('.btn-success').click()

    @allure.step('Оформить заказ')
    def place_order(self, user: User):
        self.click_place_order_button()
        self.order_modal.fill(
            user.name,
            user.country,
            user.city,
            user.credit_card,
            user.month,
            user.year,
        )

        self.order_modal.confirm()

    @allure.step('Заказ оформлен')
    def order_should_be_placed(self):
        self.order_modal.notification.should_have_successful_message()
