from models.User import User, UserInDB
from typing import Optional

class UserRepository:
    @staticmethod
    async def get_user(username: str) -> Optional[UserInDB]:
        var = await UserInDB.find_one(User.username == username)
        print(var)
        return var
