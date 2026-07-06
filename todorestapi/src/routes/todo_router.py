from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.dependency.dependency import get_todo_service
from src.schema.todo_schema import ToDoRequest
from src.service.todo_service import ToDoService

router = APIRouter(prefix="/todo",tags=["todo"])
@router.post("/")
async def create(request: ToDoRequest,todo_service:ToDoService=Depends(get_todo_service)):
   todo = await todo_service.create(request)
   return todo

#http://localhost:8000/todos/ :- GET
@router.get("/")
async def fetch_all_todos(todo_service:ToDoService=Depends(get_todo_service)):
   todo_list = await todo_service.fetch_all()
   return todo_list

# http://localhost:8000/todo/1 :- GET
@router.get("/{id}")
async def fetch_todo_by_id(id:int,todo_service:ToDoService=Depends(get_todo_service)):
  todo = await todo_service.fetch_todo_by_id(id)
  return todo



