from demoblaze_tests.utils import path
from dataclasses import dataclass
from typing import Dict, List
import csv


@dataclass
class Product:
    id: str
    name: str
    price: str
    description: str
    category: str


def get_from_file() -> List[Product]:

    with open(path(f'demoblaze_tests/data/files/products.csv')) as f:
        reader = csv.DictReader(f, delimiter=';')
        product: Dict

        products = [
            Product(
                id=product['id'],
                name=product['name'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
            )
            for product in reader
        ]

    return products


def get_by_name(value) -> Product:

    return next(
        (product for product in get_from_file() if product.name == value), None
    )


def get_by_category(value) -> List[Product]:

    return [
        product for product in get_from_file() if product.category == value
    ]
