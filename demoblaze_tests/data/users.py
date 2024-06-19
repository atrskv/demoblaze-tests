import os
from dataclasses import dataclass
from demoblaze_tests.utils import random_string
from dotenv import load_dotenv


@dataclass
class User:
    login: str
    password: str


user_with_random_credentials = User(
    login=random_string(10), password=random_string(10)
)

load_dotenv()
existing_user = User(login=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
