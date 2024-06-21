import allure
from demoblaze_tests.data import products
from demoblaze_tests.app import app
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Товары')
@allure.title('Добавление товара в корзину')
def test_add_a_product_to_the_cart():

    phone = products.phone

    app.home_page.open()
    app.home_page.products.open_card(phone.name)
    app.product_card_page.add_to_the_card()
    app.product_card_page.menu.open_cart()

    app.cart_page.cart.product_should_be_added(phone.name)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Товары')
@allure.title('Фильтрация товаров по мониторам')
def test_filter_the_products_by_monitors_category():

    app.home_page.open()
    app.home_page.products.categories.sort_by_monitors()

    app.home_page.products.should_have_sorted_by_monitors()
