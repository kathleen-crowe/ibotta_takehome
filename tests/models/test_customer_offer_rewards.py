import pytest
from datetime import datetime
from models.customer_offer_rewards import CustomerOfferReward


base_row = {
    "ID": "19964301515",
    "CUSTOMER_ID": "40446387",
    "OFFER_REWARD_ID": "768328",
    "FINISHED": "",
    "CREATED_AT": "2021-03-24 20:14:53.000",
}


def test_customer_offer_reward_basic():
    actual = CustomerOfferReward(**base_row)

    assert actual.id == 19964301515
    assert actual.customer_id == 40446387
    assert actual.offer_reward_id == 768328

    assert isinstance(actual.created_at, datetime)
    assert actual.finished is None


def test_finished_parsing():
    row = base_row.copy()
    row["FINISHED"] = "2021-03-23 22:35:26.000"

    actual = CustomerOfferReward(**row)

    assert isinstance(actual.finished, datetime)
    assert actual.finished == datetime(2021, 3, 23, 22, 35, 26)


def test_invalid_date_raises():
    row = base_row.copy()
    row["FINISHED"] = "bad-date"

    with pytest.raises(Exception):
        CustomerOfferReward(**row)