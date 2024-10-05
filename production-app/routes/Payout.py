from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List

from models.Payout import Payout, ResponseModel, ErrorResponseModel
from schemas.Payout import PayoutSchema, UpdatePayoutSchema

router = APIRouter()

@router.post("/", response_description= "Payout data added succesfully")
async def add_payout_data(payout: PayoutSchema = Body(...)):
    payout_data = payout.dict()
    new_payout = Payout(**payout_data)
    await new_payout.insert()
    return ResponseModel(data = new_payout.dict(), message= "Payout added successfully ")

@router.get("/", response_description= "Payouts retrieved sucessfully")
async def get_payout():
    payouts = await Payout.find_all().to_list()
    payout_data = [payout.dict() for payout in payouts]
    return ResponseModel(data = payout_data, message = "Payouts retrieved Successfully")

@router.get("/{id}",response_description="Payout data retrieved" )
async def get_payout_data(id:   str):
    payout = await Payout.get(id)
    if payout:
        return ResponseModel(data = payout.dict(), message="Payout data retrieved Successfully")
    raise HTTPException(status_code=404, detail=f"Payout with ID {id} not found")

@router.put("/{id}", response_description="Payout data updated successfully")
async def update_payout_data(id:str, req: UpdatePayoutSchema= Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    payout = await Payout.get(id)
    if payout:
        await payout.set(req)
        return ResponseModel(data = f"Payout with ID: {id} updated successfully",message="Payout updated successfully")
    raise HTTPException(status_code=404, detail=f"Payout with ID {id} not found")

@router.delete("/{id}", response_description="Payout deleted from database")
async def delete_payout_data(id: str):
    payout = await Payout.get(id)
    if payout:
        await payout.delete()
        return ResponseModel(data = f"Payout with ID: {id} removed ", message= "Payout deleted successfully")
    raise HTTPException(status_code=404, detail=f"Payout with ID {id} not found") 