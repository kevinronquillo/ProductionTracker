# models/Production.py
from beanie import Document
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel


# Define the Production model using Beanie
class Production(Document):
    date: datetime
    quantity: int
    hours: int
    production_list: str
    department_list: str
    comment: Optional[str] = None

    class Settings:
        collection = "productionColl"

# Success response model
class ResponseModel(BaseModel):
    data: Optional[Any]
    message: str

# Error response model
class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str
