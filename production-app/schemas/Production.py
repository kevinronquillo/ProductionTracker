from typing import Optional

from pydantic import BaseModel, Field
#from classes import SoftDeleteMixin, TimestampMixin
#from schemas import ProductionList, DepartmentList


class productionSchema(BaseModel):
    date: str = Field(...)
    quantity: int = Field(..., gt=0)
    hours: float = Field(..., gt=0)
    productionList: str = Field(...)
    departmentList: str = Field(...)
    comment: str = Field(...)

    class Config:
        schema_extra = {
            "Example": {
                "date": "12/12/2024",
                "quantity": 10,
                "hours": 3.4,
                "productionList": "Testing items for ebay",
                #     {
                #     "_id": "1",
                #     "name": "Testing Items",
                #     "createdAt": "12/12/2024",
                #     "modifiedAt": "12/12/2024",
                #     "deletedAt": None,
                #     "isDeleted": False,
                # },
                 "departmentList": "Ebay",
                    #  {
                #     "_id": "1",
                #     "name": "Ebay",
                #     "createdAt": "12/12/2024",
                #     "modifiedAt": "12/12/2024",
                #     "deletedAt": None,
                #     "isDeleted": False,
                #},
            }
        }
