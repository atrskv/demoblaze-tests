from selene.support.shared.jquery_style import s
from selene import browser
from demoblaze_tests.model.components.menu import Menu
from demoblaze_tests.utils import wait_until_alert_is_present


class ProductCardPage:
    def __init__(self):
        self.menu = Menu()

    def add_to_the_card(self):
        s('.product-content').s('.btn-success').click()

        wait_until_alert_is_present()
        browser.driver.switch_to.alert.accept()
