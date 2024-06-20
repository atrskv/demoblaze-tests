from selene import have, be
from demoblaze_tests.data import products
from demoblaze_tests.data.products import Product
from demoblaze_tests.app import app
from demoblaze_tests.data import users
import allure


def add_the_products_to_the_cart(*products: Product):

    for product in products:
        app.home_page.open()
        app.home_page.products.open_card(product.name)
        app.product_card_page.add_to_the_card()

    app.product_card_page.menu.go_home()


@allure.tag('smoke')
@allure.suite('Корзина')
@allure.title('Удаление товара из корзины')
def test_remove_a_product_from_the_cart():

    phone, laptop = products.phone, products.laptop
    add_the_products_to_the_cart(phone, laptop)

    app.home_page.menu.open_cart()
    app.cart_page.cart.remove_product(laptop.name)

    app.cart_page.cart.product(laptop.name).should(be.not_.visible)


@allure.tag('smoke')
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

    app.cart_page.order_modal.notification.title.should(
        have.text('Thank you for your purchase!')
    )
