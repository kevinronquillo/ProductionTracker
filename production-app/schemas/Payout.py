from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PayoutSchema(BaseModel):
    date: datetime
    sales: float
    listingsSold: int
    location: str
    account: str

class UpdatePayoutSchema(BaseModel):
    date: Optional[datetime] = None
    sales: Optional[float] = None
    listingsSold: Optional[int] = None
    location: Optional[str] = None