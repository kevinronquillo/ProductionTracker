from typing import Optional

from pydantic import BaseModel, Field
from classes import SoftDeleteMixin, TimestampMixin


class UpdateProduction(BaseModel):
    date: Optional[str]
    quantity: Optional[int]
    hours: Optional[float]
    productionList: object
    departmentList: object
    comment: Optional[str]

    class Config:
        schema_extra = {
            "Production Example": {
                "date": "12/12/2024",
                "quantity": 10,
                "hours": 3.4,
                "productionList": "Testing for ebay"
                    # "_id": "1",
                    # "name": "Listing Listings",
                    # "createdAt": "12/12/2024",
                    # "modifiedAt": "12/12/2024",
                    # "deletedAt": None,
                    # "isDeleted": False,
               ,
                "departmentList": "Ebay"
                #     {
                #     "_id": "1",
                #     "name": "Ebay",
                #     "createdAt": "12/12/2024",
                #     "modifiedAt": "12/12/2024",
                #     "deletedAt": None,
                #     "isDeleted": False,
                # },
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
