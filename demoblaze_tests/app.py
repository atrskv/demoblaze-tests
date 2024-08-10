from demoblaze_tests.model.pages.cart_page import CartPage
from demoblaze_tests.model.pages.home_page import HomePage
from demoblaze_tests.model.pages.product_card_page import ProductCardPage


class Application:

    def __init__(self):
        self.home_page = HomePage()
        self.cart_page = CartPage()
        self.product_card_page = ProductCardPage()


app = Application()
