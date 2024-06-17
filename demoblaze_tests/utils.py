import random
import string
from selene import browser
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def wait_until_alert_is_present():
    wait = WebDriverWait(browser.driver, 4)
    wait.until(expected_conditions.alert_is_present())
