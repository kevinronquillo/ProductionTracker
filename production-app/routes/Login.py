from fastapi import APIRouter,Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.User import User
from middleware.jwt_manager import get_current_active_user,TokenSchema
from services.AuthService import AuthService, get_auth_service


router = APIRouter()

@router.post("/token", response_model=TokenSchema)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.login(form_data.username,form_data.password)



@router.get("/users/me", response_model=User)
async def read_users_me(
    current_user: User = Depends(get_current_active_user)
):
    return current_user

@router.get("/users/me/items")
async def read_own_items(
    current_user: User =  Depends(get_current_active_user)
):
    return [{"credits": 69, "owner": current_user.username}]