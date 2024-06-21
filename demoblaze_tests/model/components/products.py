import allure
from selene.support.shared.jquery_style import s
from selene import have
from selene.core.entity import Element


class Products:
    def __init__(self, products: Element):
        self.products = products
        self.categories = Categories(s('.list-group'))

    @allure.step('Нажать на {value} в общем каталоге')
    def open_card(self, value: str):
        self.products.ss('.card-title').element_by(
            have.exact_text(value)
        ).click()

    @allure.step(
        'Товары отфильтрованы, в общем каталоге отображаются только мониторы'
    )
    def should_have_sorted_by_monitors(self):
        self.products.ss('.card-title').should(have.size(2))
        self.products.ss('.card-title').should(
            have.exact_texts('Apple monitor 24', 'ASUS Full HD')
        )


class Categories:
    def __init__(self, categories: Element):
        self.categories = categories

    @allure.step('В "Categories" нажать на "Phones"')
    def sort_by_phones(self):
        self._filter_by('Phones')

    @allure.step('В "Categories" нажать на "Laptops"')
    def sort_by_laptops(self):
        self._filter_by('laptops')

    @allure.step('В "Categories" нажать на "Monitors"')
    def sort_by_monitors(self):
        self._filter_by('Monitors')

    def _filter_by(self, value: str):
        self.categories.ss('.list-group-item').element_by(
            have.exact_text(value)
        ).click()
