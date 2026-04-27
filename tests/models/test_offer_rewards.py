from models.offer_rewards import OfferReward, OfferRewardType
import pytest
from datetime import datetime

offer_reward_row = {
    "ID": "805421",
    "OFFER_ID": "768617",
    "TYPE": "OfferReward::Instant",
    "AMOUNT": "1",
    "CREATED_AT": "2021-03-24 23:58:30.000",
    "UPDATED_AT": "2021-03-24 23:58:30.000",
}

def test_offer_reward():
    actual = OfferReward(**offer_reward_row)

    assert isinstance(actual, OfferReward)
    assert actual.id == 805421
    assert actual.offer_id == 768617
    assert actual.type == OfferRewardType.INSTANT
    assert actual.amount == 1

def test_amounts_for_large_values_and_decimal_places():
    offer_reward_row["AMOUNT"] = "1.5"

    actual = OfferReward(**offer_reward_row)

    assert actual.amount == 1.5

    offer_reward_row["AMOUNT"] = "100000000000.3333"

    actual = OfferReward(**offer_reward_row)

    assert actual.amount == 100000000000.3333

def test_datetime_parsing():
    actual = OfferReward(**offer_reward_row)

    assert isinstance(actual.created_at, datetime)
    assert actual.created_at == datetime(2021, 3, 24, 23, 58, 30)
    assert actual.updated_at == datetime(2021, 3, 24, 23, 58, 30)

def test_offer_reward_type_normalization():
    offer_reward_row["TYPE"] = "OfferReward::ShopNow"

    actual = OfferReward(**offer_reward_row)

    assert actual.type == "ShopNow"
    assert actual.type == OfferRewardType.SHOP_NOW

def test_invalid_type_raises_or_normalizes():
    offer_reward_row["TYPE"] = "OfferReward::BadType"

    with pytest.raises(ValueError):
        OfferReward(**offer_reward_row)