from typing import List
import allure
from selene.support.shared.jquery_style import s
from selene import have
from selene.core.entity import Element
from demoblaze_tests.data.products import Product


class Products:
    def __init__(self, products: Element):
        self.products = products
        self.categories = Categories(s('.list-group'))

    @allure.step('Нажать на \'{product}\' в общем каталоге')
    def open_product_card(self, product: Product):
        self.products.ss('.card-title').element_by(
            have.exact_text(product.name)
        ).click()

    @allure.step(
        'Товары отфильтрованы, в общем каталоге отображаются товары с выбранной категорией'
    )
    def should_have_filtered(self, products: List[Product]):
        products.sort(key=lambda product: product.name, reverse=True)

        self.products.ss('.card-title').should(
            have.exact_texts(*[product.name for product in products])
        )


class Categories:
    def __init__(self, categories: Element):
        self.categories = categories

    def _filter_by(self, value: str):
        self.categories.ss('.list-group-item').element_by(
            have.exact_text(value)
        ).click()

    @allure.step('В \'Categories\' нажать на \'Phones\'')
    def filter_by_phones(self):
        self._filter_by('Phones')

    @allure.step('В \'Categories\' нажать на \'Laptops\'')
    def filter_by_laptops(self):
        self._filter_by('laptops')

    @allure.step('В \'Categories\' нажать на \'Monitors\'')
    def filter_by_monitors(self):
        self._filter_by('Monitors')
