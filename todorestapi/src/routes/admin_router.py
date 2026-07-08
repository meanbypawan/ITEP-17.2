
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from src.dependency.dependency import get_admin_service
from src.schema.admin_schema import AdminRequest, AdminResponse
from src.service.admin_service import AdminService
from src.utils.jwt_util import generate_token

router = APIRouter(prefix="/admin",tags=["admin"])

#http://localhost:8000/admin/
@router.post("/",status_code=status.HTTP_201_CREATED)
async def create(request:AdminRequest,admin_service:AdminService=Depends(get_admin_service)):
    admin = await admin_service.create(request)
    return admin

@router.post("/signin",status_code=status.HTTP_200_OK,
             response_model=AdminResponse)
async def signin(request:AdminRequest,admin_service:AdminService=Depends(get_admin_service)):
    db_admin = await admin_service.signin(request)
    return AdminResponse(id=db_admin.id,
                         email=db_admin.email,
                         token=generate_token({"id":db_admin.id,"email":db_admin.email}))

