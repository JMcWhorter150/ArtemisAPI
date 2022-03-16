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
    city: str = Field(...)
    date_field: Union[date, DateQueryModel] = Field(alias="date")
    ad_count: Union[int, NumberQueryModel] = Field()
    avg_age: Union[float, int, NumberQueryModel] = Field()
    email_count: Union[int, NumberQueryModel] = Field()
    phone_count: Union[int, NumberQueryModel] = Field()

    class Config:
        schema_extra = {
            "example": {
                "city": "NEW YORK CITY",
                "date": {
                    "$gt": "2000-01-01",
                    "$lt": "2005-10-31"
                },
                "ad_count": {
                    "$gte": 10
                },
                "avg_age": 29,
                "email_count": {
                    "$lte": 50
                },
                "phone_count": 45
            }
        }

class OptionModel(BaseModel):
    sortBy: SortEnum = Field()
    limit: int = Field()
    page: int = Field()
    skip: int = Field()


class CityRequest(BaseModel):
    city: str = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "city": "ATLANTA",
                "date_from": "2022-02-15",
                "date_to": "2022-03-01"
            }
        }