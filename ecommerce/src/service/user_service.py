from fastapi import HTTPException

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import User
from src.repository.user_repository import UserRepository
from src.schema.user_schema import UserRequest, UserLoginRequest
from src.util.password_util import hash_password, verify_password


class UserService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo = user_repo

    async def create_user(self,request:UserRequest):
        user = User(
            name=request.name,
            email=request.email,
            password=hash_password(request.password),
            contact=request.contact
        )
        return await self.user_repo.create(user)
    async def authenticate(self,request:UserLoginRequest):
        user = await self.user_repo.fetch_by_email(request.email)
        if not user:
            raise HTTPException(status_code=404, detail="Incorrect email | Email not found")
        status = verify_password(request.password,user.password)
        if not status:
            raise HTTPException(status_code=401, detail="Incorrect password")
        return user