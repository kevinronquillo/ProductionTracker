from datetime import datetime,timedelta,timezone
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jwt import decode,encode
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from models.User import User
from repositories.UserRepository import UserRepository
from classes.Settings import Settings
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import BaseModel

settings = Settings()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseSettings):
    access_token: str
    token_type: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    username: Optional[str] = None

def create_access_token(data: dict, expires_delta: Optional[timedelta]= None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})
    return encode(to_encode,settings.SECRET_KEY, algorithm=settings.ALGORITHM)

async def get_current_user(token: str =  Depends(oauth_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        payload = decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = await UserRepository.get_user(username)
        if user is None:
            raise credentials_exception
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Token has expired",
                            headers={"WWW-Authenticate":"Bearer"}
                            
                            )
    except InvalidTokenError:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail= "Inactive user")
    return current_user
    