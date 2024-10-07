# schemas/Production.py
from pydantic import BaseModel,constr
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):

    username: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    credits: Optional[int] = None
    city: Optional[str] = None
    password:str
    
class UpdateUserSchema(BaseModel):

    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    credits: Optional[int] = None
    city: Optional[str] = None
    
class UserInDBSchema(UserSchema):
    hashed_password: str
    
