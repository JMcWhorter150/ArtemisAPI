from typing import Optional
from datetime import date

from pydantic import BaseModel, EmailStr, Field


class CityCountModel(BaseModel):
    city: str = Field(...)
    date: date = Field(...)
    ad_count: int = Field(...)
    avg_age: float = Field()
    email_count: int = Field()
    phone_count: int = Field()

    class Config:
        schema_extra = {
            "example": {
                "id": "6221455240741654807e19af",
                "city": "TALLAHASSEE",
                "date": "2022-02-28",
                "ad_count": 65,
                "avg_age": 26.615384615384617,
                "email_count": 0,
                "phone_count": 50,
            }
        }

