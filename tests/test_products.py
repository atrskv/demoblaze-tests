from selene import browser, have
from selene.support.shared.jquery_style import s
from demoblaze_tests.utils import wait_until_alert_is_present
from demoblaze_tests.data import products


def test_add_a_product_to_the_cart():

    # GIVEN
    phone = products.phone
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#tbodyid').ss('.card-title').element_by(
        have.exact_text(phone.name)
    ).click()

    s('.product-content').s('.btn-success').click()

    # AND
    wait_until_alert_is_present()
    browser.driver.switch_to.alert.accept()

    s('.navbar-nav').s('#cartur').click()

    # THEN
    s('#tbodyid').ss('tr').first.ss('td').second.should(
        have.exact_text(phone.name)
    )

    s('#totalp').should(have.exact_text(phone.price))


def test_filter_the_products_by_monitors_category():

    # GIVEN
    monitor = products.monitor
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('.list-group').ss('.list-group-item').element_by(
        have.exact_text('Monitors')
    ).click()

    # THEN
    cards = s('#tbodyid').ss('.card-title')
    cards.should(have.size(2))
    cards.second.should(have.exact_text(monitor.name))
