# models/Production.py
from beanie import Document
from typing import Optional, Any
from datetime import date
from pydantic import BaseModel


class Payout(Document):
    date: date
    sales: float
    listingsSold: int
    location: str
    account: str

# Success response model
class ResponseModel(BaseModel):
    data: Optional[Any]
    message: str

# Error response model
class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str
