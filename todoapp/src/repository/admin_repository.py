from sqlalchemy import select

from src.model.admin import Admin
class AdminRepository:
    def __init__(self,session):
        self.session = session

    async def save(self,admin:Admin):
        self.session.add(admin)
        await self.session.flush()
        await self.session.refresh(admin)
        return admin

    async def get_admin_by_email(self,email:str):
        statement = select(Admin).where(Admin.email == email)
        result = await self.session.execute(statement)
        print(result)
        return result.scalar_one_or_none()
