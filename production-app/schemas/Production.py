# schemas/Production.py
from pydantic import BaseModel
from typing import Optional
from datetime import date as fecha

# Schema for creating a new production entry
class ProductionSchema(BaseModel):
    date: fecha
    quantity: int
    hours: int
    production_list: str
    comment: Optional[str] = None
    employeeId:Optional[str] = None

# Schema for updating a production entry (fields optional)
class UpdateProductionSchema(BaseModel):
    date: Optional[fecha] = None
    quantity: Optional[int] = None
    hours: Optional[int] = None
    production_list: Optional[str] = None
    comment: Optional[str] = None
