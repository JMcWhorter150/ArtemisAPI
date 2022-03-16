from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

class CityAdModel(BaseModel):
    city: str = Field(...)
    ads: int = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "city": "TALLAHASSEE",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "ads": 65,
            }
        }

class CityCountModel(BaseModel):
    city: str = Field(...)
    date_field: date = Field(..., alias="date")
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

class CityEmailModel(BaseModel):
    city: str = Field(...)
    emails: int = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "city": "TALLAHASSEE",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "emails": 0,
            }
        }

class CityPhoneModel(BaseModel):
    city: str = Field(...)
    phones: int = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "city": "TALLAHASSEE",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "phones": 6,
            }
        }

class CityAdResponse(BaseModel):
    data: CityAdModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "city": "TALLAHASSEE",
                    "date_from": "2022-01-01",
                    "date_to": "2022-03-01",
                    "ads": "4123"
                },
                "code": 200,
                "message": "City ad data retrieved successfully"
            }
        }

class CityPhoneResponse(BaseModel):
    data: CityPhoneModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "city": "MIAMI",
                    "date_from": "2022-01-01",
                    "date_to": "2022-01-07",
                    "phones": "94"
                },
                "code": 200,
                "message": "City phone data retrieved successfully"
            }
        }

class CityEmailResponse(BaseModel):
    data: CityEmailModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "city": "BISMARCK",
                    "date_from": "2022-01-01",
                    "date_to": "2022-01-02",
                    "emails": "0"
                },
                "code": 200,
                "message": "No results found"
            }
        }

class CityCountResponse(BaseModel):
    data: CityCountModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "id": "6221455240741654807e19af",
                    "state": "Debuke",
                    "date": "2022-02-28",
                    "ad_count": 17,
                    "avg_age": 26,
                    "email_count": 0,
                    "phone_count": 14,
            },
                "code": 200,
                "message": "City trafficking data found"
            }
        }