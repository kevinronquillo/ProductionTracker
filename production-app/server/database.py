# server/database.py
import motor.motor_asyncio
from beanie import init_beanie
from models.Production import Production
from models.ProductionCategory import ProductionCategory
from models.Payout import Payout
from models.User import User
from dotenv import load_dotenv
import os
# Database connection details
load_dotenv()
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_DETAILS"))
database = client.production

# Initialize Beanie
async def init_db():
    await init_beanie(database=database, document_models=[Production,ProductionCategory,Payout,User])
