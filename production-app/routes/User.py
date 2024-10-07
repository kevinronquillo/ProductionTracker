from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from models.User import User,ResponseModel, ErrorResponseModel, UserInDB
from schemas.User import UserSchema, UpdateUserSchema
from middleware.security import get_password_hash
from repositories.UserRepository import UserRepository

router = APIRouter()

@router.post("/", response_description="User data added succesfully")
async def add_user_data(user: UserSchema = Body(...)):
    user_data = user.dict()
    new_user = User(**user_data)
    await  new_user.insert()
    return ResponseModel(data = user.dict(), message= "User added successfully" )

@router.get("/", response_description="Useres retrieved successfully")
async def get_user():
    users = await UserInDB.find_all().to_list()
    user_data = [user.dict() for user in users]
    return ResponseModel(data =user_data , message= "Users retrieved Successfully")

@router.get("/{id}", response_description="User data retrieved")
async def get_user_data(id: str ):
    user  = await User.get(id)
    if user:
        return ResponseModel(data = user.dict(),message="User data retrieved successfully")
    raise HTTPException(status_code=404, detail=f"User with ID {id} not found")

@router.put("/{id}", response_description="User data updated successfully")
async def update_user_data(id: str, req: UpdateUserSchema= Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    user = await User.get(id)
    if user:
        await user.set(req)
        return ResponseModel(data = f"User with id: {id} updated successfully", message= "User updated successfully")
    raise HTTPException(status_code=404, detail=f"User with ID {id} not found")

@router.delete("/{id}", response_description= "User deleted from database")
async def delete_user_data(id: str):
    user = await User.get(id)
    if user:
        await user.delete()
        return ResponseModel(data =f"User with ID: {id} removed", message="User deleted successfully")
    raise HTTPException(status_code=404, detail=f"User with ID {id} not found")

@router.post("/register",response_description="User created succesfully")
async def register_user(user: UserSchema):
    existingUser = await UserRepository.get_user(user.username)
    if existingUser:
        HTTPException(status_code=400, detail="Username already exists")
        
    hashed_password = get_password_hash(user.password)
    
    new_user = UserInDB(
        
        username = user.username,
        firstName= user.firstName,
        lastName= user.lastName,
        credits= user.credits,
        hashed_password =hashed_password,
        city= user.city,
        disabled= False
    )
    await new_user.insert()
    return{"msg": f"User for: {user.firstName} {user.lastName} created successfully"}