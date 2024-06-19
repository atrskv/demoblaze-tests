from selene import by, have, browser, be
from selene.support.shared.jquery_style import s
from demoblaze_tests.data import products
from demoblaze_tests.data.products import Product
from demoblaze_tests.utils import wait_until_alert_is_present


def put_the_products_into_the_cart(*products: Product):

    for product in products:
        browser.open('https://www.demoblaze.com')

        s('#tbodyid').ss('.card-title').element_by(
            have.exact_text(product.name)
        ).click()
        s('.product-content').s('.btn-success').click()

        wait_until_alert_is_present()
        browser.driver.switch_to.alert.accept()

    s('.navbar-nav').ss('.nav-item').element_by(have.text('Home')).click()


def test_remove_a_product_from_the_cart():

    # GIVEN
    phone = products.phone
    laptop = products.laptop

    put_the_products_into_the_cart(phone, laptop)

    # WHEN
    s('.navbar-nav').s('#cartur').click()

    # AND
    s('#tbodyid').ss('tr.success').element_by(have.text(laptop.name)).s(
        by.link_text('Delete')
    ).click()

    # THEN
    s('#tbodyid').ss('tr.success').element_by(have.text(laptop.name)).should(
        be.visible
    )


def test_place_a_purchase_order():

    # GIVEN
    phone = products.phone
    laptop = products.laptop

    put_the_products_into_the_cart(phone, laptop)

    s('.navbar-nav').s('#cartur').click()

    # WHEN
    s('.btn-success').click()
    s('#name').type('Aleksei')
    s('#country').type('Russia')
    s('#city').type('City')
    s('#card').type('123321 441')
    s('#month').type('12')
    s('#year').type('1233')
    s('#orderModal').s('.btn-primary').click()

    # THEN
    s('.sweet-alert').s('h2').should(have.text('Thank you for your purchase!'))
