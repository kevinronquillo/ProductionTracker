# schemas/Production.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for creating a new production entry
class ProductionSchema(BaseModel):
    date: datetime
    quantity: int
    hours: int
    production_list: str
    department_list: str
    comment: Optional[str] = None

# Schema for updating a production entry (fields optional)
class UpdateProductionSchema(BaseModel):
    date: Optional[datetime]
    quantity: Optional[int]
    hours: Optional[int]
    production_list: Optional[str]
    department_list: Optional[str]
    comment: Optional[str]
