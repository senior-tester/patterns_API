import requests
import pytest
from test_data import payloads, headers
from endpoints.create_booking import CreateBooking
from endpoints.update_booking import UpdateBooking
import os


@pytest.fixture()
def authorize():
    token = os.getenv('API_TOKEN')
    if not token:
        response = requests.post(
            'https://restful-booker.herokuapp.com/auth',
            json=payloads.credentials,
            headers=headers.default_header
        )
        token = response.json()['token']
        os.environ['API_TOKEN'] = token
    return {'Cookie': f'token = {token}'}


@pytest.fixture()
def new_booking(authorize):
    create = CreateBooking()
    create.create_booking()
    yield create.data.bookingid
    requests.delete(
        f'https://restful-booker.herokuapp.com/booking/{create.data.bookingid}',
        headers=headers.default_header.update(authorize)
    )


@pytest.fixture()
def new_booking_endp():
    return CreateBooking()


@pytest.fixture()
def upd_endpoint(authorize):
    return UpdateBooking(authorize)
