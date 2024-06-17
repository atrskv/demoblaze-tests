from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: str
    description: str


phone = Product(
    name='Iphone 6 32gb',
    description='''It comes with 1GB of RAM. 
             The phone packs 16GB of internal storage cannot be expanded. 
             As far as the cameras are concerned, the Apple iPhone 6 
             packs a 8-megapixel primary camera on the rear and 
             a 1.2-megapixel front shooter for selfies.''',
    price='790',
)


monitor = Product(
    name='ASUS Full HD',
    description='ASUS VS247H-P 23.6- Inch Full HD',
    price='230',
)
