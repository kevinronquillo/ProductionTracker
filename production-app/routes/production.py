# routes/production.py
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List

from models.Production import Production, ResponseModel, ErrorResponseModel
from schemas.Production import ProductionSchema, UpdateProductionSchema

router = APIRouter()

# Create (POST) - Add a new production
@router.post("/", response_description="Production data added successfully")
async def add_production_data(production: ProductionSchema = Body(...)):
    production_data = production.dict()  # Extract the dictionary from the Pydantic model
    new_production = Production(**production_data)  # Initialize Beanie's Production model with keyword arguments
    await new_production.insert()  # Insert into MongoDB
    return ResponseModel(data = new_production.dict(), message= "Production added successfully.")

# Read (GET) - Retrieve all productions
@router.get("/", response_description="Productions retrieved successfully")
async def get_productions():
    productions = await Production.find_all().to_list()
    # Convert each Production object to dictionary
    production_data = [production.dict() for production in productions]
    return ResponseModel(data=production_data, message="Productions data retrieved successfully.")


# Read (GET) - Retrieve a single production by ID
@router.get("/{id}", response_description="Production data retrieved")
async def get_production_data(id: str):
    production = await Production.get(id)
    if production:
        return ResponseModel(production.dict(), "Production data retrieved successfully")
    raise HTTPException(status_code=404, detail=f"Production with ID {id} not found.")

# Update (PUT) - Update production data
@router.put("/{id}", response_description="Production data updated successfully")
async def update_production_data(id: str, req: UpdateProductionSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}  # Ignore None values
    production = await Production.get(id)
    if production:
        await production.set(req)
        return ResponseModel(f"Production with ID: {id} updated successfully", "Production updated successfully")
    raise HTTPException(status_code=404, detail=f"Production with ID {id} not found.")

# Delete (DELETE) - Delete a production by ID
@router.delete("/{id}", response_description="Production deleted from the database")
async def delete_production_data(id: str):
    production = await Production.get(id)
    if production:
        await production.delete()
        return ResponseModel(f"Production with ID: {id} removed", "Production deleted successfully")
    raise HTTPException(status_code=404, detail=f"Production with ID {id} not found.")
