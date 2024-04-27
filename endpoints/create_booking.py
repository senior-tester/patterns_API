from test_data import payloads, headers
import requests
from endpoints.json_schemas import NewBooking
from endpoints.base_endpoint import BaseEndpoint


class CreateBooking(BaseEndpoint):

    def create_booking(self, payload=None):
        payload = payload if payload else payloads.default_payload
        self.response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=payload,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = NewBooking(**self.response.json())

    def check_firstname(self, firstname):
        assert self.data.booking.firstname == firstname

    def check_lastname(self, lastname):
        assert self.data.booking.lastname == lastname
