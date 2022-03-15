from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class StatePhoneModel(BaseModel):
    state: str = Field()
    phones: int = Field()
    date_from: date = Field()
    date_to: date = Field()

    class Config:
        schema_extra = {
            "example": {
                "state": "MINNESOTA",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "phones": 19,
            }
        }
