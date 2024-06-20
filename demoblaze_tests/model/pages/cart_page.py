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

    def open(self):
        browser.open('/cart.html')

    def place_order(self):
        s('.btn-success').click()
