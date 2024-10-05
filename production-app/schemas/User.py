# schemas/Production.py
from pydantic import BaseModel,constr
from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):

    username: str
    firstName: str
    lastName: str
    password: str
    credits: int
    city: str


    
class UpdateUserSchema(BaseModel):

    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    password: Optional[str] = None
    credits: Optional[int] = None
    city: Optional[str] = None
