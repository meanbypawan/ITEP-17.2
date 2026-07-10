from fastapi import Depends

from src.dependency.repository_dependency import get_user_repository
from src.repository.user_repository import UserRepository
from src.service.user_service import UserService


def get_user_service(user_repo:UserRepository=Depends(get_user_repository)):
    return UserService(user_repo)