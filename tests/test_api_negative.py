import requests
from test_data import payloads, headers
from endpoints.create_booking import CreateBooking


def test_update_booking_negative(authorize, new_booking):
    headers.default_header.update(authorize)
    response = requests.put(
        f'https://restful-booker.herokuapp.com/booking/{new_booking}',
        json=payloads.without_depositpaid,
        headers=headers.default_header
    )
    assert response.status_code == 400


def test_create_booking_negative():
    new_booking_endp = CreateBooking()
    new_booking_endp.create_booking(payload=payloads.without_depositpaid)
    new_booking_endp.check_response_is_500()
