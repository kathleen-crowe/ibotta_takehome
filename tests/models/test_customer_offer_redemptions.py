import pytest
from datetime import datetime
from models.customer_offer_redemptions import CustomerOfferRedemption


base_row = {
    "ID": "692578410",
    "CUSTOMER_OFFER_ID": "19955759064",
    "VERIFIED_REDEMPTION_COUNT": "1",
    "SUBMITTED_REDEMPTION_COUNT": "1",
    "OFFER_AMOUNT": "1.5",
    "CREATED_AT": "2021-03-22 08:32:25.000",
}


def test_customer_offer_redemption_basic():
    obj = CustomerOfferRedemption(**base_row)

    assert obj.id == 692578410
    assert obj.customer_offer_id == 19955759064

    assert obj.verified_redemption_count == 1
    assert obj.submitted_redemption_count == 1

    assert obj.offer_amount == 1.5

    assert isinstance(obj.created_at, datetime)


def test_missing_values_become_none():
    row = base_row.copy()
    row["VERIFIED_REDEMPTION_COUNT"] = ""
    row["SUBMITTED_REDEMPTION_COUNT"] = ""
    row["OFFER_AMOUNT"] = ""

    obj = CustomerOfferRedemption(**row)

    assert obj.verified_redemption_count is None
    assert obj.submitted_redemption_count is None
    assert obj.offer_amount is None


def test_invalid_datetime_raises():
    row = base_row.copy()
    row["CREATED_AT"] = "bad-date"

    with pytest.raises(Exception):
        CustomerOfferRedemption(**row)