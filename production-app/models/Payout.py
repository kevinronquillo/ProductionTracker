# models/Production.py
from beanie import Document
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel


class Payout(Document):
    date: datetime
    sales: float
    listingsSold: int

# Success response model
class ResponseModel(BaseModel):
    data: Optional[Any]
    message: str

# Error response model
class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str
