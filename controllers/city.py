from database.database import city_collection
from utils.utils import paginate

async def query_city_counts(filter, options) -> dict:
    return await paginate(filter, options, city_collection)

async def query_city_ads(city, date_from, date_to) -> dict:
    ads = 0
    async for ad in city_collection.find({"city": city, "date": {"$gte": date_from, "$lt": date_to}}):
        ads += ad['ad_count']
    return {
        'city': city,
        'date_from': date_from,
        'date_to': date_to,
        'ads': ads
        }

async def query_city_phones(city, date_from, date_to) -> dict:
    phones = 0
    async for phone in city_collection.find({"city": city, "date": {"$gte": date_from, "$lt": date_to}}):
        phones += phone['phone_count']
    return {
        'city': city,
        'date_from': date_from,
        'date_to': date_to,
        'phones': phones
        }

async def query_city_emails(city, date_from, date_to) -> dict:
    emails = 0
    async for email in city_collection.find({"city": city, "date": {"$gte": date_from, "$lt": date_to}}):
        emails += email['email_count']
    return {
        'city': city,
        'date_from': date_from,
        'date_to': date_to,
        'emails': emails
        }