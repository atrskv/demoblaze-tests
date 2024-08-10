import base64
from uuid import uuid4
import requests
import settings
from demoblaze_tests.data.products import Product
from selene import browser
from demoblaze_tests.data.users import User
from demoblaze_tests.utils import (
    request_logs,
    response_logs,
)


class ApiClient:

    def __init__(self):
        self.api_url = settings.config.api_url
        self.session = requests.Session()

    def _request(
        self,
        endpoint,
        method,
        data=None,
        params=None,
        json_data=None,
        allow_redirects=False,
    ):
        url = f'{self.api_url}{endpoint}'

        response = self.session.request(
            method,
            url,
            data=data,
            params=params,
            json=json_data,
            allow_redirects=allow_redirects,
        )

        request_logs(response)
        response_logs(response)

        return response

    def add_products_to_cart(self, *products: Product):

        cookie = str(uuid4())

        for product in products:

            payload = {
                "id": str(uuid4()),
                "cookie": f"user={cookie}",
                "prod_id": product.id,
                "flag": False,
            }

            self._request(
                endpoint='/addtocart',
                method='POST',
                json_data=payload,
            )

        browser.open('/')
        browser.driver.add_cookie({'name': 'user', 'value': cookie})
        browser.driver.refresh()

    def sign_up(self, user: User):

        payload = {
            "username": user.login,
            "password": base64.b64encode(user.password.encode('ascii')).decode(
                'ascii'
            ),
        }

        self._request(
            endpoint='/signup',
            method='POST',
            json_data=payload,
        )
