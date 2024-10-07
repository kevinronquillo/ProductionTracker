from beanie import Document
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel
from pydantic_settings import BaseSettings

class User(Document):

    username: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    credits: Optional[int] = None
    city: Optional[str] = None
    disabled: Optional[bool] = None

# Success response model
class ResponseModel(BaseModel):
    data: Optional[Any]
    message: str

# Error response model
class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str

class UserInDB(User):
    hashed_password: str
    
