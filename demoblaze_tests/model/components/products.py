from selene.support.shared.jquery_style import s, ss
from selene import have
from selene.core.entity import Element


class Products:
    def __init__(self, products: Element):
        self.products = products
        self.categories = Categories(s('.list-group'))

    def open_card(self, value: str):
        self.products.ss('.card-title').element_by(
            have.exact_text(value)
        ).click()

    @property
    def cards(self):
        return self.products.ss('.card-title')


class Categories:
    def __init__(self, categories: Element):
        self.categories = categories

    def sort_by_phones(self):
        self._filter_by('Phones')

    def sort_by_laptops(self):
        self._filter_by('laptops')

    def sort_by_monitors(self):
        self._filter_by('Monitors')

    def _filter_by(self, value: str):
        self.categories.ss('.list-group-item').element_by(
            have.exact_text(value)
        ).click()
