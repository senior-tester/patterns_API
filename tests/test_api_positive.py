import requests
from test_data import payloads, headers


def test_create_booking(new_booking_endp):
    new_booking_endp.create_booking()
    new_booking_endp.check_response_is_200()
    new_booking_endp.check_firstname(payloads.default_payload['firstname'])
    new_booking_endp.check_lastname(payloads.default_payload['lastname'])


def test_update_booking(new_booking, upd_endpoint):
    upd_endpoint.update(payloads.updated_first_name, new_booking)
    upd_endpoint.check_response_is_200()
    upd_endpoint.check_data('firstname', payloads.updated_first_name['firstname'])
    upd_endpoint.check_data('lastname', payloads.updated_first_name['lastname'])


def test_get_booking(new_booking):
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{new_booking}')
    data = response.json()
    assert response.status_code == 200
    assert data['totalprice'] == 1000
