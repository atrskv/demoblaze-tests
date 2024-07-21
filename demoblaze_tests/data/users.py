from mimesis import Person, Address, Payment, Datetime
from dataclasses import dataclass
from typing import Optional
import config


@dataclass
class User:
    login: str
    password: str
    name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    credit_card: Optional[str] = None
    month: Optional[str] = None
    year: Optional[int] = None


def generate() -> User:

    person = Person()
    address = Address()
    payment = Payment()
    datetime = Datetime()

    return User(
        login=person.username(),
        password=person.password(),
        name=person.full_name(),
        country=address.country(),
        city=address.city(),
        credit_card=payment.credit_card_number(),
        month=datetime.month(),
        year=datetime.year(),
    )


def get_existing() -> User:

    return User(
        login=config.login,
        password=config.password,
        name=config.name,
        country=config.country,
        city=config.city,
        credit_card=config.credit_card,
        month=config.month,
        year=config.year,
    )
