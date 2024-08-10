from dataclasses import dataclass
from typing import Dict, List
import csv
from demoblaze_tests.utils import path


@dataclass
class Product:
    id: int
    name: str
    price: str
    description: str
    category: str

    def __repr__(self) -> str:
        return str(self.name)


def _get_products_from_file() -> List[Product]:

    with open(path(f'demoblaze_tests/data/files/products.csv')) as f:
        reader = csv.DictReader(f, delimiter=';')
        product: Dict

        products = [
            Product(
                id=int(product['id']),
                name=product['name'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
            )
            for product in reader
        ]

    return products


class Catalog:
    def __init__(self, products: List[Product]):
        self.products = products

    def by_id(self, value: int) -> Product:
        return next(
            (
                product
                for product in _get_products_from_file()
                if product.id == value
            ),
            None,
        )

    def by_ids(self, *values: int) -> List[Product]:
        return [
            product
            for product in _get_products_from_file()
            if product.id in values
        ]

    def by_name(self, value: str) -> Product:
        return next(
            (
                product
                for product in _get_products_from_file()
                if product.name == value
            ),
            None,
        )

    def by_names(self, *values: str) -> List[Product]:
        return [
            product
            for product in _get_products_from_file()
            if product.name in values
        ]

    def by_category(self, value: str) -> List[Product]:
        return [
            product
            for product in _get_products_from_file()
            if product.category == value
        ]


catalog = Catalog(_get_products_from_file())
