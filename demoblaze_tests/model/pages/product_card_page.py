import allure
from selene.support.shared.jquery_style import s
from selene import browser
from demoblaze_tests.data.products import Product
from demoblaze_tests.model.components.menu import Menu
from demoblaze_tests.model.components.modal_content import Alert


class ProductCardPage:
    def __init__(self):
        self.menu = Menu()
        self.alert = Alert()

    @allure.step('Открыть карточку товара \'{product}\'')
    def open(self, product: Product):
        browser.open(f'/prod.html?idp_={product.id}')

    @allure.step('В карточке товара нажать на кнопку \'Add to cart\'')
    def add_product_to_cart(self):
        s('.product-content').s('.btn-success').click()
        self.alert.accept()
