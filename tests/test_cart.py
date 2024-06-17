from selene import browser
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s, ss
from demoblaze_tests.utils import wait_until_alert_is_present
from demoblaze_tests.data.products import monitor, phone


def test_remove_a_product_from_the_cart(cart):

    # WHEN
    s('.navbar-nav').s('#cartur').click()

    # AND
    s('#tbodyid').ss('tr.success').first.ss(
        by.link_text('Delete')
    ).first.click()

    # THEN
    s('#tbodyid').should(have.no.css_class('success'))


def test_place_a_purchase_order(cart):
    s('.navbar-nav').s('#cartur').click()

    s('.btn-success').click()

    s('#name').type('Aleksei')

    s('#country').type('Russia')

    s('#city').type('City')

    s('#card').type('123321 441')

    s('#month').type('12')

    s('#year').type('1233')

    s('#orderModal').s('.btn-primary').click()

    s('.sweet-alert').s('h2').should(have.text('Thank you for your purchase!'))
