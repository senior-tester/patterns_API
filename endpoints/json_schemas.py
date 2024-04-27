from pydantic import BaseModel


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: dict
    additionalneeds: str


class NewBooking(BaseModel):
    bookingid: int
    booking: Booking
