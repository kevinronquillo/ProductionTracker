from beanie import Document
from typing import Optional, Any
from pydantic import BaseModel

class ProductionCategory(Document):
    title: str

    
class ResponseModel(BaseModel):
    data: Optional[Any]
    message: str

# Error response model
class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str