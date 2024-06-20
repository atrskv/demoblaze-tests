from selene import have
from demoblaze_tests.data import products
from demoblaze_tests.app import app


def test_add_a_product_to_the_cart():

    phone = products.phone

    app.home_page.open()
    app.home_page.products.open_card(phone.name)
    app.product_card_page.add_to_the_card()
    app.product_card_page.menu.open_cart()

    app.cart_page.cart.name_of_added_product.should(
        have.exact_text(phone.name)
    )


def test_filter_the_products_by_monitors_category():

    monitor = products.monitor

    app.home_page.open()
    app.home_page.products.categories.sort_by_monitors()

    app.home_page.products.cards.should(have.size(2)).second.should(
        have.exact_text(monitor.name)
    )
