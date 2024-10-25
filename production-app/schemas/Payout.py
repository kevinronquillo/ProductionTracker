from pydantic import BaseModel
from typing import Optional
from datetime import date as fecha


class PayoutSchema(BaseModel):
    date: fecha
    sales: float
    listingsSold: int
    location: str
    account: str

class UpdatePayoutSchema(BaseModel):
    date: Optional[fecha] = None
    sales: Optional[float] = None
    listingsSold: Optional[int] = None
    location: Optional[str] = None