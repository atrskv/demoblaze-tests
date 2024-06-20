import os
from dataclasses import dataclass
from demoblaze_tests.utils import random_string
from dotenv import load_dotenv
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


user_with_random_credentials = User(
    login=random_string(10), password=random_string(10)
)

load_dotenv()
existing_user = User(
    login=os.getenv('LOGIN'),
    password=os.getenv('PASSWORD'),
    name=os.getenv('NAME'),
    country=os.getenv('COUNTRY'),
    city=os.getenv('CITY'),
    credit_card=os.getenv('CREDIT_CARD'),
    month=os.getenv('MONTH'),
    year=os.getenv('YEAR'),
)
