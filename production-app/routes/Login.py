from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.User import User, ResponseModel
from middleware.jwt_manager import get_current_active_user, TokenSchema
from services.AuthService import AuthService, get_auth_service

router = APIRouter()

@router.post("/token", response_model=TokenSchema, summary="Login and get an access token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
) -> TokenSchema:
    return await auth_service.login(form_data.username, form_data.password)


@router.get("/user/me/credits", response_model=ResponseModel, summary="Get current user's credits")
async def get_user_credits(
    current_user: User = Depends(get_current_active_user)
) -> ResponseModel:
    credits = current_user.credits or 0
    return ResponseModel(data={"credits": credits}, message="User credits retrieved successfully")


@router.get("/user/me", response_model=ResponseModel, summary="Get current user details")
async def read_users_me(
    current_user: User = Depends(get_current_active_user)
) -> ResponseModel:
    user_data = {
        "username": current_user.username,
        "firstName": current_user.firstName,
        "lastName": current_user.lastName,
        "credits": current_user.credits,
        "city": current_user.city,
        "role": current_user.role,
        "disabled": current_user.disabled
    }
    return ResponseModel(data=user_data, message="User data retrieved successfully")
