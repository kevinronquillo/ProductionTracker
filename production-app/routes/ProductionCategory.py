from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List

from models.ProductionCategory import ProductionCategory,ResponseModel,ErrorResponseModel
from schemas.ProductionCategory import ProductionCategorySchema, UpdateProductionCategorySchema


router = APIRouter()
#Post For New 

@router.post("/", response_description="Production category added succesfully")
async def add_category_data(productionCategory: ProductionCategorySchema = Body(...)):
    productionCategory_data = productionCategory.dict()
    new_productionCategory = ProductionCategory(**productionCategory_data)
    await new_productionCategory.insert()
    return ResponseModel(data = new_productionCategory.dict(), message= "Production Category added succesfully")

#Get all Categories

@router.get("/", response_description="Production categories retrieved succesfully")
async def get_Categories():
    categories = await ProductionCategory.find_all().to_list()
    #convert productions to dicts
    category_data = [category.dict() for category in categories]
    return ResponseModel(data= category_data, message="Production Categories retrieved succesfully")

#Get Categories by ID

@router.get("/{id}", response_description="Category data retrieved")
async def get_category_data(id: str):
    category = await ProductionCategory.get(id)
    if category:
        return ResponseModel(data = category.dict(), message= "Category data retrieved succesfully")
    raise HTTPException(status_code=404, detail="Production Category with ID {id} not found.")
 
#Update(PUT) Categories
@router.put("/{id}", response_description="Production data updated succefully")
async def update_category_data(id: str, req: UpdateProductionCategorySchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    category = await ProductionCategory.get(id)
    if category:
        await category.set(req)
        return ResponseModel(data= f"Production category with ID: {id} updated successfully", message= "Production Category updated" )
    raise HTTPException(status_code=404, detail="Production category with ID {id} not found")

#Delete a production ID

@router.delete("/{id}", response_description="Category deleted from database")
async def delete_category_data(id: str):
    category = await ProductionCategory.get(id)
    if category:
        await category.delete()
        return ResponseModel(data = f"Category with ID: {id} removed", message="Category deleted successfully")
    HTTPException(status_code=404 , detail=f"Category with ID {id} not found")