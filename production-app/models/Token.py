from pydantic_settings import BaseSettings
from pydantic import BaseModel
from typing import Optional

class Token(BaseSettings):
    access_token: str
    token_type: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    username: Optional[str] = None