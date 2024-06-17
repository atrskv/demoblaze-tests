from selene import browser, have
from selene.support.shared.jquery_style import s
from demoblaze_tests.utils import wait_until_alert_is_present
from demoblaze_tests.data.products import monitor, phone


def test_add_a_product_to_the_cart():

    # GIVEN
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('#tbodyid').ss('.card-title').element_by(
        have.exact_text(phone.name)
    ).click()

    s('.product-content').s('.btn-success').click()

    # AND
    wait_until_alert_is_present()
    browser.driver.switch_to.alert.accept()

    s('#navbarExample').s('#cartur').click()

    # THEN
    s('#tbodyid').ss('tr.success').first.ss('td').second.should(
        have.exact_text(phone.name)
    )


def test_filter_the_products_by_monitors_category():

    # GIVEN
    browser.open('https://www.demoblaze.com')

    # WHEN
    s('.list-group').ss('.list-group-item').element_by(
        have.exact_text('Monitors')
    ).click()

    # THEN
    s('#tbodyid').ss('.card-title').should(have.size(2))
    s('#tbodyid').ss('.card-title').second.should(
        have.exact_text(monitor.name)
    )
