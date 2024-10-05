from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PayoutSchema(BaseModel):
    date: datetime
    sales: float
    listingsSold: int

class UpdatePayoutSchema(BaseModel):
    date: Optional[datetime]
    sales: Optional[float]
    listingsSold: Optional[int]