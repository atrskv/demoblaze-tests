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


laptop = Product(
    name='Sony vaio i5',
    description='''Sony is so confident that the VAIO S is 
            a superior ultraportable laptop that the company 
            proudly compares the notebook to Apple's 13-inch MacBook Pro. 
            And in a lot of ways this notebook is better, 
            thanks to a lighter weight.''',
    price='790',
)
