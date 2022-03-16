from fastapi import APIRouter, Query
from datetime import date
from models.admin import ResponseModel
from models.state_request import OptionModel, FilterModel
from models.state_response import StateAdResponse, StateEmailResponse, StatePhoneResponse, StateCountResponse
from controllers.state import query_state_counts, query_state_ads, query_state_emails, query_state_phones

router = APIRouter()

@router.get("/counts", response_description="Total data about state scrapes")
async def get_counts(filter: FilterModel, options: OptionModel) -> StateCountResponse:
    counts = await query_state_counts(filter, options)
    return ResponseModel(counts, 'State count data retrieved successfully') \
        if counts['totalResults'] > 0 \
        else ResponseModel(
            counts, "No results found"
        )

@router.get("/ads", response_description="Get just total ads for state for date range")
async def get_ads(state: str, date_from: date, date_to: date) -> StateAdResponse:
    ads = await query_state_ads(state, date_from, date_to)
    return ResponseModel(ads, 'State ad data retrieved successfully') \
        if len(ads["ads"]) > 0 \
        else ResponseModel(
            ads, "No results found"
        )

@router.get("/phones", response_description="Get just total phones for state for date range")
async def get_phones(state: str, date_from: date, date_to: date) -> StatePhoneResponse:
    phones = await query_state_phones(state, date_from, date_to)
    return ResponseModel(phones, 'State ad data retrieved successfully') \
        if len(phones["phones"]) > 0 \
        else ResponseModel(
            phones, "No results found"
        )

@router.get("/emails", response_description="Get just total emails for state for date range")
async def get_emails(state: str, date_from: date, date_to: date) -> StateEmailResponse:
    emails = await query_state_emails(state, date_from, date_to)
    return ResponseModel(emails, 'State ad data retrieved successfully') \
        if len(emails["emails"]) > 0 \
        else ResponseModel(
            emails, "No results found"
        )