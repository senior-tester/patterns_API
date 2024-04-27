from endpoints.create_booking import CreateBooking
from endpoints.update_booking import UpdateBooking
import requests
from test_data import payloads, headers


class BaseTest:

    def setup_method(self):
        self.new_booking_endp = CreateBooking()
        self.upd_endpoint = UpdateBooking(self.get_token())

    def get_token(self):
        response = requests.post(
            'https://restful-booker.herokuapp.com/auth',
            json=payloads.credentials,
            headers=headers.default_header
        )
        token = response.json()['token']
        return {'Cookie': f'token = {token}'}
