from typing import Optional
from datetime import date
from enum import IntEnum
from pydantic import BaseModel, Field    

class StateAdModel(BaseModel):
    state: str = Field(...)
    ads: int = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "state": "FLORIDA",
                "date_from": "2022-02-28",
                "date_to": "2022-03-09",
                "ads": 65,
            }
        }

class StateCountModel(BaseModel):
    state: str = Field(...)
    date_field: date = Field(..., alias="date")
    ad_count: int = Field(...)
    avg_age: float = Field()
    email_count: int = Field()
    phone_count: int = Field()

    class Config:
        schema_extra = {
            "example": {
                "id": "6221455240741654807e19af",
                "state": "IDAHO",
                "date": "2022-02-28",
                "ad_count": 17,
                "avg_age": 31.615384615384617,
                "email_count": 0,
                "phone_count": 8,
            }
        }

class StateEmailModel(BaseModel):
    state: str = Field(...)
    emails: int = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "state": "MASSACHUSETTS",
                "date_from": "2022-02-28",
                "date_to": "2022-03-05",
                "emails": 191,
            }
        }

class StatePhoneModel(BaseModel):
    state: str = Field(...)
    phones: int = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "state": "OREGON",
                "date_from": "2022-01-28",
                "date_to": "2022-01-31",
                "phones": 191,
            }
        }

class StateAdResponse(BaseModel):
    data: StateAdModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "state": "WASHINGTON",
                    "date_from": "2022-01-01",
                    "date_to": "2022-03-01",
                    "ads": "7123"
                },
                "code": 200,
                "message": "State ad data retrieved successfully"
            }
        }

class StatePhoneResponse(BaseModel):
    data: StatePhoneModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "state": "ALABAMA",
                    "date_from": "2022-01-01",
                    "date_to": "2022-01-07",
                    "phones": "31"
                },
                "code": 200,
                "message": "State phone data retrieved successfully"
            }
        }

class StateEmailResponse(BaseModel):
    data: StateEmailModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "state": "WYOMING",
                    "date_from": "2022-01-01",
                    "date_to": "2022-01-02",
                    "emails": "0"
                },
                "code": 200,
                "message": "No results found"
            }
        }

class StateCountResponse(BaseModel):
    data: StateCountModel = Field()
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "id": "6221455240741654807e19af",
                    "state": "IDAHO",
                    "date": "2022-02-28",
                    "ad_count": 17,
                    "avg_age": 31.615384615384617,
                    "email_count": 0,
                    "phone_count": 8,
            },
                "code": 200,
                "message": "State trafficking data found"
            }
        }