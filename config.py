import os
from dotenv import load_dotenv

load_dotenv()

selenoid_login = os.getenv('SELENOID_LOGIN')
selenoid_pass = os.getenv('SELENOID_PASS')
selenoid_url = os.getenv('SELENOID_URL')

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
name = os.getenv('NAME')
country = os.getenv('COUNTRY')
city = os.getenv('CITY')
credit_card = os.getenv('CREDIT_CARD')
month = os.getenv('MONTH')
year = os.getenv('YEAR')
