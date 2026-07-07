import email

from src.model import Admin
from src.repository.admin_repository import AdminRepository
from src.schema.admin_schema import AdminRequest
from src.utils.password import hash_password


class AdminService:
    def __init__(self,admin_repo:AdminRepository):
        self.admin_repo = admin_repo

    async def create(self,request:AdminRequest):
        admin = Admin(email=request.email,password=hash_password(request.password))
        return await self.admin_repo.create(admin)
