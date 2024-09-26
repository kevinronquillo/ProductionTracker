from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieveProductions,
    addProduction,
    getProduction,
    updateProduction,
    deleteProduction,
)
from schemas.Production import productionSchema

from models.Production import UpdateProduction, ResponseModel, ErrorResponseModel

router = APIRouter()


@router.post("/", response_description="Production Data Added")
async def addProductionData(production: productionSchema = Body(...)):
    production = jsonable_encoder(production)
    newProduction = await addProduction(production)
    return ResponseModel(newProduction, "Production added successfully")
