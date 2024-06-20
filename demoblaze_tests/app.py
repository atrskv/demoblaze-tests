from demoblaze_tests.model.pages.cart_page import CartPage
from demoblaze_tests.model.pages.home_page import HomePage
from demoblaze_tests.model.pages.product_card_page import ProductCardPage


class Application:
    home_page = HomePage()
    cart_page = CartPage()
    product_card_page = ProductCardPage()


app = Application()
