import motor.motor_asyncio
from bson import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.artemis

admin_collection = database.get_collection('admins')
city_collection = database.get_collection('city_count')
state_collection = database.get_collection('state_count')