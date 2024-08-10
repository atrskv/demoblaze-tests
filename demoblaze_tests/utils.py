import logging
from requests import Response
from selene import browser
from allure_commons.types import AttachmentType
import allure
import settings
import demoblaze_tests
from pathlib import Path


def path(file) -> str:
    return str(Path(demoblaze_tests.__file__).parent.parent.joinpath(file))


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='Screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


def add_browser_logs():
    log = ''.join(
        f'{text}\n' for text in browser.driver.get_log(log_type='browser')
    )
    allure.attach(log, 'Browser logs', AttachmentType.TEXT, '.log')


def add_html():
    html = browser.driver.page_source
    allure.attach(html, 'Page source', AttachmentType.HTML, '.html')


def add_video():
    video_url = (
        f'https://{settings.config.selenoid_url}/video/'
        + browser.driver.session_id
        + ".mp4"
    )
    html = (
        '<html><body><video width=\'100%\' height=\'100%\' controls autoplay><source src='
        + video_url
        + ' type=\'video/mp4\'></video></body></html>'
    )
    allure.attach(
        html,
        'Video. Session id: ' + browser.driver.session_id,
        AttachmentType.HTML,
        '.html',
    )


def request_logs(response: Response):
    logging.info('Request: ' + response.request.url)
    logging.info('Request method: ' + response.request.method)
    logging.info('Request headers: ' + str(response.request.headers))
    if response.request.body:
        logging.info('INFO Request body: ' + str(response.request.body))


def response_logs(response: Response):
    logging.info('Response code: ' + str(response.status_code))
    logging.info('Response headers: ' + str(response.headers))
    if response.text:
        logging.info('INFO Response body: ' + response.text)
