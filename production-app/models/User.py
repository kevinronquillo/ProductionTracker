from beanie import Document
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel


class User(Document):

    username: str
    firstName: str
    lastName: str
    password: str
    credits: int
    city: str

# Success response model
class ResponseModel(BaseModel):
    data: Optional[Any]
    message: str

# Error response model
class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str
