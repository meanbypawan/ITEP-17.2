from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.service_dependency import get_user_service
from src.schema.user_schema import UserRequest

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/",
             status_code=status.HTTP_201_CREATED)

async def create_user(request:UserRequest,user_service = Depends(get_user_service)):
    return await user_service.create_user(request)

