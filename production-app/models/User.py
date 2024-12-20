from beanie import Document
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from classes.SoftDeleteMixin import SoftDeleteMixin
from classes.TimestampMixin import TimestampMixin
from bson import ObjectId



class User(Document):
    
    username: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    credits: Optional[int] = None
    city: Optional[str] = None
    role: Optional[str] = None
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

class UserInDB(User,SoftDeleteMixin,TimestampMixin):
    hashed_password: str
