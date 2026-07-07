
from fastapi import APIRouter, Depends
from starlette import status

from src.dependency.dependency import get_admin_service
from src.schema.admin_schema import AdminRequest
from src.service.admin_service import AdminService

router = APIRouter(prefix="/admin",tags=["admin"])

#http://localhost:8000/admin/
@router.post("/",status_code=status.HTTP_201_CREATED)
async def create(request:AdminRequest,admin_service:AdminService=Depends(get_admin_service)):
    admin = await admin_service.create(request)
    return admin

