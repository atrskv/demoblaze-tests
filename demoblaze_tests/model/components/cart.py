from selene.support.shared.jquery_style import s
from selene import by, have


class Cart:
    def __init__(self):
        self.cart = s('#tbodyid')
        self._products = self.cart.ss('tr.success')

    def remove_product(self, value: str):
        self._products.element_by(have.text(value)).s(
            by.link_text('Delete')
        ).click()

    def product(self, value):
        return self._products.element_by(have.text(value))

    @property
    def products(self):
        return self._products

    @property
    def name_of_added_product(self):
        return self._products.first.ss('td').second
