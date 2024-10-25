from middleware.security import verify_password
from middleware.jwt_manager import create_access_token, settings, Token
from repositories.UserRepository import UserRepository
from datetime import timedelta
from models.User import UserInDB
from fastapi import HTTPException, status
from typing import Optional

class AuthService:
    def __init__(self,user_repo: UserRepository):
        self.user_repo = user_repo
        
    async def authenticate_user(self, username: str, password: str) -> Optional[UserInDB]:
        user = await self.user_repo.get_user(username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user
    
    async def login(self, username: str, password: str ) -> Token:
        user =  await self.authenticate_user(username, password)
        if not user: 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
        access_token = create_access_token(data= {
            "sub": user.username,"id": str(user.id)}, 
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        return Token(access_token=access_token, token_type="bearer")

def get_auth_service() -> AuthService:
    return AuthService(user_repo=UserRepository())