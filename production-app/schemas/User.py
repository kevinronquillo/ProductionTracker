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

    username: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    password: Optional[str]
    credits: Optional[int]
    city: Optional[str]
