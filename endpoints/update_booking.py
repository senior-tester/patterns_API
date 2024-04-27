import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint


class UpdateBooking(BaseEndpoint):

    def __init__(self, token):
        self.token = token

    def update(self, payload, booking_id):
        headers.default_header.update(self.token)
        self.response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{booking_id}',
            json=payload,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = self.response.json()

    def check_data(self, key, value):
        assert self.data[key] == value
