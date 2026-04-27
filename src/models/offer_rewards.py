from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from enum import Enum
from models.datetime_validator import parse_datetime

class OfferRewardType(str, Enum):
    FACT = "Fact"
    SHOP_NOW = "ShopNow"
    POLL = "Poll"
    POLLMULTI = "PollMulti"
    INSTANT = "Instant"
    VIDEO = "Video"
    RECIPE = "Recipe"
    VIDEOAD = "VideoAd"
    JOUST = "Joust"
    QUIZ = "Quiz"
    ENGAGEMENT = "Engagement"
    TESTIFY = "Testify"
    DOGOODER = "DoGooder"
    SEALOFAPPROVAL = "SealOfApproval"
    NUTRITION = "Nutrition"
    HOWTO = "HowTo"

    @classmethod
    def _missing_(cls, value):
        # # Normalizing: "OfferReward::Instant" → "Instant"
        if isinstance(value, str) and value.startswith("OfferReward::"):
            value = value.split("::")[1]
            return cls(value)


class OfferReward(BaseModel):
    id: int = Field(alias="ID")
    offer_id: int = Field(alias="OFFER_ID")
    type: OfferRewardType = Field(alias="TYPE")
    amount: float = Field(alias="AMOUNT")
    created_at: datetime = Field(alias="CREATED_AT")
    updated_at: datetime = Field(alias="UPDATED_AT")

    @field_validator("created_at", "updated_at", mode="before")
    def parse_dates(cls, v):
        return parse_datetime(v)