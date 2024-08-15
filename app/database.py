from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URL = os.getenv(
    "MONGODB_URL",
    "mongodb://logging-mongodb.hfu5mq8dph6eg.us-east-1.cs.amazonlightsail.com:27018/logging_db",
)
client = AsyncIOMotorClient(MONGODB_URL)
database = client["logging_db"]
log_collection = database["logs"]
