# routes/production.py
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from schemas.User import UserSchema
from models.Production import Production, ResponseModel, ErrorResponseModel
from schemas.Production import ProductionSchema, UpdateProductionSchema
from repositories.UserRepository import UserRepository

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
        return ResponseModel(data = production.dict(), message = "Production data retrieved successfully")
    raise HTTPException(status_code=404, detail=f"Production with ID {id} not found.")

# Update (PUT) - Update production data
@router.put("/{id}", response_description="Production data updated successfully")
async def update_production_data(id: str, req: UpdateProductionSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}  # Ignore None values
    production = await Production.get(id)
    if production:
        await production.set(req)
        return ResponseModel(data = f"Production with ID: {id} updated successfully", message="Production updated successfully")
    raise HTTPException(status_code=404, detail=f"Production with ID {id} not found.")

# Delete (DELETE) - Delete a production by ID
@router.delete("/{id}", response_description="Production deleted from the database")
async def delete_production_data(id: str):
    production = await Production.get(id)
    if production:
        await production.delete()
        return ResponseModel(data = f"Production with ID: {id} removed", message = "Production deleted successfully")
    raise HTTPException(status_code=404, detail=f"Production with ID {id} not found.")
# Get all the productions from one employee
@router.get("/employee/{employeeId}", response_description="Production data retrieved")
async def get_productions_by_employee(employeeId: str):
    # Use .find with a filter and to_list to convert to a list of documents
    productions = await Production.find({"employeeId": employeeId}).to_list(length=None)  # None retrieves all documents

    if productions:
        return ResponseModel(data=[production.dict() for production in productions], message="Production data retrieved successfully")
    
    raise HTTPException(status_code=404, detail=f"No productions found for employee ID {employeeId}")