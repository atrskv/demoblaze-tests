import allure
from demoblaze_tests.app import app
from allure_commons.types import Severity


@allure.severity(Severity.CRITICAL)
@allure.suite('Корзина')
@allure.title('Удаление товара из корзины')
def test_remove_a_product_from_the_cart(given_cart_with_products):

    *_, laptop = given_cart_with_products

    app.home_page.menu.select_cart_tab()
    app.cart_page.cart.remove_product(laptop)

    app.cart_page.cart.product_should_be_removed(laptop)


@allure.severity(Severity.CRITICAL)
@allure.suite('Корзина')
@allure.title('Оформление заказа')
def test_place_an_order(given_generated_user, given_cart_with_products):

    _ = given_cart_with_products
    user = given_generated_user

    app.cart_page.open()
    app.cart_page.place_order(user)

    app.cart_page.order_should_be_placed()
