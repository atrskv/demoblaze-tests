from demoblaze_tests.model.components.menu import Menu
from demoblaze_tests.model.components.modal_content import (
    SignUpModal,
    LogInModal,
)
from selene.support.shared.jquery_style import s
from selene import browser
from demoblaze_tests.model.components.products import (
    Products,
)


class HomePage:
    def __init__(self):
        self.menu = Menu()
        self.sign_up_modal = SignUpModal(s('#signInModal'))
        self.log_in_modal = LogInModal(s('#logInModal'))
        self.products = Products(s('#tbodyid'))

    def open(self):
        browser.open('/')
