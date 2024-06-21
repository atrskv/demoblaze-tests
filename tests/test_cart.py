import allure
from demoblaze_tests.data import products
from demoblaze_tests.app import app
from demoblaze_tests.data import users
from allure_commons.types import Severity
from demoblaze_tests.utils import add_the_products_to_the_cart


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Корзина')
@allure.title('Удаление товара из корзины')
def test_remove_a_product_from_the_cart():

    phone, laptop = products.phone, products.laptop
    add_the_products_to_the_cart(phone, laptop)

    app.home_page.menu.open_cart()
    app.cart_page.cart.remove_product(laptop.name)

    app.cart_page.cart.product_should_be_removed(laptop.name)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Корзина')
@allure.title('Оформление заказа')
def test_place_a_purchase_order():

    phone, laptop = products.phone, products.laptop
    user = users.existing_user
    add_the_products_to_the_cart(phone, laptop)

    app.home_page.menu.open_cart()
    app.cart_page.place_order()
    app.cart_page.order_modal.fill(
        user.name,
        user.country,
        user.city,
        user.credit_card,
        user.month,
        user.year,
    )
    app.cart_page.order_modal.confirm()

    app.cart_page.order_modal.notification.should_have_successful_message()
