# server/database.py
import motor.motor_asyncio
from beanie import init_beanie
from models.Production import Production
from models.ProductionCategory import ProductionCategory
from models.Payout import Payout
from models.User import User
# Database connection details
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.production

# Initialize Beanie
async def init_db():
    await init_beanie(database=database, document_models=[Production,ProductionCategory,Payout,User])
