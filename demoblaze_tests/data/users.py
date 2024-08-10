from mimesis import Person, Address, Payment, Datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    login: str
    password: str
    name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    credit_card: Optional[str] = None
    month: Optional[str] = None
    year: Optional[str] = None

    def __repr__(self) -> str:
        return str(self.login)


def generate() -> User:

    return User(
        login=Person().username(),
        password=Person().password(),
        name=Person().full_name(),
        country=Address().country(),
        city=Address().city(),
        credit_card=Payment().credit_card_number(),
        month=Datetime().month(),
        year=str(Datetime().year()),
    )
