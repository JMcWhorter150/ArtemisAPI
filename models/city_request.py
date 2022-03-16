from typing import Union
from enum import Enum
from pydantic import BaseModel, Field
from datetime import date

class DateQueryModel(BaseModel):
    gt: date = Field(default=None, alias='$gt')
    lt: date = Field(default=None, alias='$lt')
    gte: date = Field(default=None, alias='$gte')
    lte: date = Field(default=None, alias='$lte')

    class Config:
        schema_extra = {
            "example": {
                "$gt": "2000-01-01",
                "$lte": "2011-01-01"
            }
        }

class NumberQueryModel(BaseModel):
    gt: Union[int, float, None] = Field(alias='$gt')
    lt: Union[int, float, None] = Field(alias='$lt')
    gte: Union[int, float, None] = Field(alias='$gte')
    lte: Union[int, float, None] = Field(alias='$lte')

    class Config:
        schema_extra = {
            "example": {
                "$gt": "15",
                "$lte": "24"
            }
        }


class FilterModel(BaseModel):
    city: str = Field(...)
    date_field: Union[date, DateQueryModel, None] = Field(alias="date")
    ad_count: Union[int, NumberQueryModel, None] = Field()
    avg_age: Union[float, int, NumberQueryModel, None] = Field()
    email_count: Union[int, NumberQueryModel, None] = Field()
    phone_count: Union[int, NumberQueryModel, None] = Field()

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
    # TODO: need validation in form key:asc or key:desc as str
    sortBy: str = Field()
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

class CityCountBody(BaseModel):
    filter: FilterModel = Field(...)
    options: OptionModel = Field(...)
