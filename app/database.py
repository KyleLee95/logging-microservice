from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27018")
client = AsyncIOMotorClient(MONGODB_URL)
database = client["logging_db"]
log_collection = database["logs"]
