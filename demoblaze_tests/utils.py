from selene import browser
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os
import allure
from allure_commons.types import AttachmentType
import demoblaze_tests
from pathlib import Path

# from demoblaze_tests.data.products import Product


def path(file) -> str:

    return str(Path(demoblaze_tests.__file__).parent.parent.joinpath(file))


def wait_until_alert_is_present():

    wait = WebDriverWait(browser.driver, 4)
    wait.until(expected_conditions.alert_is_present())


# def add_the_products_to_the_cart(*products: Product):
#
#     for product in products:
#         browser.open('/')
#
#         s('#tbodyid').ss('.card-title').element_by(
#             have.exact_text(product.name)
#         ).click()
#         s('.product-content').s('.btn-success').click()
#
#         wait_until_alert_is_present()
#         browser.driver.switch_to.alert.accept()
#
#     s('.navbar-nav').ss('.nav-item').element_by(have.text('Home')).click()


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


def add_logs():
    log = "".join(
        f'{text}\n' for text in browser.driver.get_log(log_type='browser')
    )
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html():
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video():
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
