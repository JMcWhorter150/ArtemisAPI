import motor.motor_asyncio
from bson import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection('students_collection')
admin_collection = database.get_collection('admins')
