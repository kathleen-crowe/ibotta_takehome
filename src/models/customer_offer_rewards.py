from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

from models.datetime_validator import parse_datetime

class CustomerOfferReward(BaseModel):
    id: int = Field(alias="ID")
    customer_id: int = Field(alias="CUSTOMER_ID")
    offer_reward_id: int = Field(alias="OFFER_REWARD_ID")
    finished: Optional[datetime] = Field(default=None, alias="FINISHED")
    created_at: datetime = Field(alias="CREATED_AT")

    @field_validator("finished","created_at", mode="before")
    def parse_dates(cls, v):
        return parse_datetime(v)