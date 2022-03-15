from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class CityAdModel(BaseModel):
    city: str = Field()
    ads: int = Field()
    date_from: date = Field()
    date_to: date = Field()

    class Config:
        schema_extra = {
            "example": {
                "city": "TALLAHASSEE",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "ads": 65,
            }
        }
