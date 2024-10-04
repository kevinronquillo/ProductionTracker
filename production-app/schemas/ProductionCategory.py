from typing import Optional

from pydantic import BaseModel, Field

#from classes import SoftDeleteMixin, TimestampMixin

class ProductionCategorySchema(BaseModel):
    title: str

class UpdateProductionCategorySchema(BaseModel):
    title: Optional[str]