from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.repository.category_repository import CategoryRepository
from src.repository.user_repository import UserRepository


def get_user_repository(session:AsyncSession=Depends(get_session)):
    return UserRepository(session)

def get_category_repository(session:AsyncSession=Depends(get_session)):
    return CategoryRepository(session)