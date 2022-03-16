from database.database import state_collection
from utils.utils import paginate

async def query_state_counts(filter, options) -> dict:
    return await paginate(filter, options, state_collection)

async def query_state_ads(state, date_from, date_to) -> dict:
    ads = 0
    async for ad in state_collection.find({"state": state, "date": {"$gte": date_from, "$lt": date_to}}):
        ads += ad['ad_count']
    return {
        'state': state,
        'date_from': date_from,
        'date_to': date_to,
        'ads': ads
        }

async def query_state_phones(state, date_from, date_to) -> dict:
    phones = 0
    async for phone in state_collection.find({"state": state, "date": {"$gte": date_from, "$lt": date_to}}):
        phones += phone['phone_count']
    return {
        'state': state,
        'date_from': date_from,
        'date_to': date_to,
        'phones': phones
        }

async def query_state_emails(state, date_from, date_to) -> dict:
    emails = 0
    async for email in state_collection.find({"state": state, "date": {"$gte": date_from, "$lt": date_to}}):
        emails += email['email_count']
    return {
        'state': state,
        'date_from': date_from,
        'date_to': date_to,
        'emails': emails
        }