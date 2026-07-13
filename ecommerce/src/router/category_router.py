from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.params import Form
from starlette import status

from src.dependency.service_dependency import get_category_service
from src.service.category_service import CategoryService

router = APIRouter(prefix="/category",tags=["Category"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_category(category_name:str=Form(...),
                          category_image:UploadFile=File(...),
                          category_service:CategoryService = Depends(get_category_service)):
   return await category_service.create(category_name,category_image)

@router.get("/",status_code=status.HTTP_200_OK)
async def fetch_all(category_service:CategoryService = Depends(get_category_service)):
   return await category_service.fetch_all()