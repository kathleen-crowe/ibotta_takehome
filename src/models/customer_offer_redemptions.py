from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

from models.datetime_validator import parse_datetime


class CustomerOfferRedemption(BaseModel):
    id: int = Field(alias="ID")
    customer_offer_id: int = Field(alias="CUSTOMER_OFFER_ID")
    verified_redemption_count: Optional[int] = Field(default=None, alias="VERIFIED_REDEMPTION_COUNT")
    submitted_redemption_count: Optional[int] = Field(default=None, alias="SUBMITTED_REDEMPTION_COUNT")
    offer_amount: Optional[float] = Field(default=None, alias="OFFER_AMOUNT")
    created_at: datetime = Field(alias="CREATED_AT")

    @field_validator(
        "created_at",
        "verified_redemption_count",
        "submitted_redemption_count",
        "offer_amount",
        mode="before"
    )
    def clean_fields(cls, v, info):
        if v in ("", None):
            return None

        field = info.field_name

        if field == "created_at":
            return parse_datetime(v)

        if field in ("verified_redemption_count", "submitted_redemption_count"):
            return int(v)

        if field == "offer_amount":
            return float(v)

        return v