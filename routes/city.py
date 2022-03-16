from fastapi import APIRouter, Query
from datetime import date
from models.admin import ResponseModel
from models.city_request import OptionModel, FilterModel, CityRequest
from models.city_response import CityAdResponse, CityEmailResponse, CityPhoneResponse, CityCountResponse
from controllers.city import query_city_counts, query_city_ads, query_city_emails, query_city_phones

router = APIRouter()

@router.get("/counts", response_description="Total data about city scrapes")
async def get_counts(filter: FilterModel, options: OptionModel) -> CityCountResponse:
    counts = await query_city_counts(filter, options)
    return ResponseModel(counts, 'City count data retrieved successfully') \
        if counts['totalResults'] > 0 \
        else ResponseModel(
            counts, "No results found"
        )

@router.get("/ads", response_description="Get just total ads for city for date range")
async def get_ads(city: str, date_from: date, date_to: date) -> CityAdResponse:
    ads = await query_city_ads(city, date_from, date_to)
    return ResponseModel(ads, 'City ad data retrieved successfully') \
        if len(ads["ads"]) > 0 \
        else ResponseModel(
            ads, "No results found"
        )

@router.get("/phones", response_description="Get just total phones for city for date range")
async def get_phones(city: str, date_from: date, date_to: date) -> CityPhoneResponse:
    phones = await query_city_phones(city, date_from, date_to)
    return ResponseModel(phones, 'City phone data retrieved successfully') \
        if len(phones["phones"]) > 0 \
        else ResponseModel(
            phones, "No results found"
        )

@router.get("/emails", response_description="Get just total emails for city for date range")
async def get_emails(city: str, date_from: date, date_to: date) -> CityEmailResponse:
    emails = await query_city_emails(city, date_from, date_to)
    return ResponseModel(emails, 'City email data retrieved successfully') \
        if len(emails["emails"]) > 0 \
        else ResponseModel(
            emails, "No results found"
        )