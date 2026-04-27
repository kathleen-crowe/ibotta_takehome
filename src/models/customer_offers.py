from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional


class CustomerOffer(BaseModel):
    id: int = Field(alias="ID")
    customer_id: int = Field(alias="CUSTOMER_ID")
    offer_id: int = Field(alias="OFFER_ID")
    activated: Optional[datetime] = Field(default=None, alias="ACTIVATED")
    verified: Optional[datetime] = Field(default=None, alias="VERIFIED")

    @field_validator("activated", "verified", mode="before")
    def parse_datetime(cls, v):
        if v in ("", None):
            return None
        return datetime.fromisoformat(v.replace(" ", "T"))