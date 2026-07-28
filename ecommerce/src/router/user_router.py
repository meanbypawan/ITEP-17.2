from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.service_dependency import get_user_service
from src.schema.user_schema import UserRequest, UserLoginRequest, UserResponse
from src.service.user_service import UserService
from src.util.jwt_util import generate_token

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/",
             status_code=status.HTTP_201_CREATED)

async def create_user(request:UserRequest,user_service = Depends(get_user_service)):
    return await user_service.create_user(request)

@router.post("/signin",status_code=status.HTTP_200_OK,
             response_model=UserResponse)
async def authenticate_user(request:UserLoginRequest,user_service:UserService=Depends(get_user_service)):
    user = await user_service.authenticate(request)
    return UserResponse(id=user.id,
                        name=user.name,
                        email=user.email,
                        contact=user.contact,
                        token=generate_token({"id":user.id,"email":user.email})
                        )
