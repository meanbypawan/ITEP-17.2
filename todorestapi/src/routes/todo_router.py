from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.schema.todo_schema import ToDoRequest
from src.service.todo_service import ToDoService

router = APIRouter(prefix="/todo",tags=["todo"])

@router.post("/")
async def create(request: ToDoRequest,session:AsyncSession=Depends(get_session)):
   todo_service = ToDoService(session)
   todo = await todo_service.create(request)
   return todo

