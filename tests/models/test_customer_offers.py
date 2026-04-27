import pytest
from models.customer_offers import CustomerOffer
from datetime import datetime

customer_offer_row_not_verified = {
    "ID": "19964301515",
    "CUSTOMER_ID": "40446387",
    "OFFER_ID": "768328",
    "ACTIVATED": "2021-03-24 20:14:53.000",
    "VERIFIED": ""
}

customer_offer_row_verified = {
    "ID": "19962356611",
    "CUSTOMER_ID": "40424372",
    "OFFER_ID": "755100",
    "ACTIVATED": "2021-03-23 21:45:16.000",
    "VERIFIED": "2021-03-23 22:35:26.000"
}

def test_valid_customer_offer():
    actual = CustomerOffer(**customer_offer_row_not_verified)

    assert actual.id == 19964301515
    assert actual.customer_id == 40446387
    assert actual.offer_id == 768328
    assert isinstance(actual.activated, datetime)
    assert actual.verified is None

    values = actual.model_dump()

    assert values["verified"] is None

def test_verified_value():
    actual = CustomerOffer(**customer_offer_row_verified)

    assert isinstance(actual.verified, datetime) 
    assert actual.verified == datetime(2021, 3, 23, 22, 35, 26)               

def test_invalid_date():
    customer_offer_row_not_verified["ACTIVATED"] = "bad-date"

    with pytest.raises(Exception):
        CustomerOffer(**customer_offer_row_not_verified)

    customer_offer_row_verified["VERIFIED"] = "bad-date"
    with pytest.raises(Exception):
        CustomerOffer(**customer_offer_row_verified)