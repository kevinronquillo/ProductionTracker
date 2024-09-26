from typing import Optional

from pydantic import BaseModel, Field

#from classes import SoftDeleteMixin, TimestampMixin

class ProductionList(BaseModel):
    title: str = Field(...)

