from fastapi import Depends

from src.dependency.repository_dependency import get_user_repository, get_category_repository
from src.repository.category_repository import CategoryRepository
from src.repository.user_repository import UserRepository
from src.service.category_service import CategoryService
from src.service.user_service import UserService


def get_user_service(user_repo:UserRepository=Depends(get_user_repository)):
    return UserService(user_repo)

def get_category_service(category_repo:CategoryRepository = Depends(get_category_repository)):
    return CategoryService(category_repo)