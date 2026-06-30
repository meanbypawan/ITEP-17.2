from src.exception.resouce_not_found_exception import ResourceNotFoundException
from src.model import Admin
from src.repository.admin_repository import AdminRepository
from src.utils.password import verify_password


class AdminService:
    def __init__(self,session):
        self.admin_repo = AdminRepository(session)

    async def save(self,admin):
        return await self.admin_repo.save(admin)

    async def authenticate(self,admin:Admin):
        db_admin = await self.admin_repo.get_admin_by_email(admin.email)
        if not db_admin:
          raise ResourceNotFoundException(f"Invalid email id | Not found")
        status = verify_password(admin.password,db_admin.password)
        return status
