from typing import Optional
from datetime import date

from pydantic import BaseModel, EmailStr, Field


class StateAdModel(BaseModel):
    state: str = Field()
    ads: int = Field()
    date_from: date = Field()
    date_to: date = Field()

    class Config:
        schema_extra = {
            "example": {
                "state": "NEVADA",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "ads": 1204,
            }
        }
