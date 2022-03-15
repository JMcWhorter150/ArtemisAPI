from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class StateCountModel(BaseModel):
    state: str = Field(...)
    date: date = Field(...)
    ad_count: int = Field(...)
    avg_age: float = Field()
    email_count: int = Field()
    phone_count: int = Field()

    class Config:
        schema_extra = {
            "example": {
                "city": "MONTANA",
                "date": "2022-03-01",
                "ad_count": 13,
                "avg_age": 29,
                "email_count": 0,
                "phone_count": 6,
            }
        }

