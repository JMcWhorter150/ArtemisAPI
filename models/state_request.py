from typing import Union
from enum import Enum
from pydantic import BaseModel, Field
from datetime import date

class SortEnum(str, Enum):
    asc = 'asc'
    desc = 'desc'

class DateQueryModel(BaseModel):
    gt: date = Field(alias='$gt')
    lt: date = Field(alias='$lt')
    gte: date = Field(alias='$gte')
    lte: date = Field(alias='$lte')

    class Config:
        schema_extra = {
            "example": {
                "$gt": "2000-01-01",
                "$lte": "2011-01-01"
            }
        }

class NumberQueryModel(BaseModel):
    gt: Union[int, float] = Field(alias='$gt')
    lt: Union[int, float] = Field(alias='$lt')
    gte: Union[int, float] = Field(alias='$gte')
    lte: Union[int, float] = Field(alias='$lte')

    class Config:
        schema_extra = {
            "example": {
                "$gt": "15",
                "$lte": "24"
            }
        }


class FilterModel(BaseModel):
    state: str = Field(...)
    date_filter: Union[date, DateQueryModel] = Field(alias="date")
    ad_count: Union[int, NumberQueryModel] = Field()
    avg_age: Union[float, int, NumberQueryModel] = Field()
    email_count: Union[int, NumberQueryModel] = Field()
    phone_count: Union[int, NumberQueryModel] = Field()

    class Config:
        schema_extra = {
            "example": {
                "state": "NEW YORK",
                "date": {
                    "$gt": "2000-01-01",
                    "$lt": "2005-09-31"
                },
                "ad_count": {
                    "$gte": 17
                },
                "avg_age": 21,
                "email_count": {
                    "$lte": 90
                },
                "phone_count": 400
            }
        }

class OptionModel(BaseModel):
    sortBy: SortEnum = Field()
    limit: int = Field()
    page: int = Field()
    skip: int = Field()


class StateRequest(BaseModel):
    state: str = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "state": "GEORGIA",
                "date_from": "2022-02-19",
                "date_to": "2022-02-28"
            }
        }