from fastapi import HTTPException

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Admin
from src.repository.admin_repository import AdminRepository
from src.schema.admin_schema import AdminRequest
from src.utils.password import hash_password, verify_password


class AdminService:
    def __init__(self,admin_repo:AdminRepository):
        self.admin_repo = admin_repo

    async def create(self,request:AdminRequest):
        admin = Admin(email=request.email,password=hash_password(request.password))
        return await self.admin_repo.create(admin)

    async def signin(self,request:AdminRequest):
        db_admin = await self.admin_repo.fetch_by_email(request.email)
        if not db_admin:
            raise ResourceNotFoundException(f"Invalid email {request.email}")
        status = verify_password(request.password,db_admin.password)
        if not status:
            raise HTTPException(status_code=401,detail="Invalid password")
        return db_admin