import random
import string
from selene import browser
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os
import allure
from allure_commons.types import AttachmentType


def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def wait_until_alert_is_present():
    wait = WebDriverWait(browser.driver, 4)
    wait.until(expected_conditions.alert_is_present())


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


def add_logs(browser):
    log = "".join(
        f'{text}\n' for text in browser.driver.get_log(log_type='browser')
    )
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = (
        f"https://{os.getenv('SELENOID_URL')}/video/"
        + browser.driver.session_id
        + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        html,
        'video_' + browser.driver.session_id,
        AttachmentType.HTML,
        '.html',
    )
