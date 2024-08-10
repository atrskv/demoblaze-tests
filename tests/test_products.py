import allure
from demoblaze_tests.app import app
from allure_commons.types import Severity


@allure.severity(Severity.CRITICAL)
@allure.suite('Товары')
@allure.title('Добавление товара в корзину')
def test_add_a_product_to_the_cart(given_products):

    phone = given_products.by_name('HTC One M9')

    app.home_page.open()
    app.home_page.products.open_product_card(phone)
    app.product_card_page.add_product_to_cart()
    app.product_card_page.menu.select_cart_tab()

    app.cart_page.cart.product_should_be_added(phone)


@allure.severity(Severity.CRITICAL)
@allure.suite('Товары')
@allure.title('Фильтрация товаров по мониторам')
def test_filter_the_products_by_monitors_category(given_products):

    monitors = given_products.by_category('monitors')

    app.home_page.open()
    app.home_page.products.categories.filter_by_monitors()

    app.home_page.products.should_have_filtered(monitors)
