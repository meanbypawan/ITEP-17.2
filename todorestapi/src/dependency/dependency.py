from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.repository.todo_repository import ToDoRepository
from src.service.todo_service import ToDoService

def get_todo_repository(session:AsyncSession=Depends(get_session)):
    return ToDoRepository(session)

def get_todo_service(session:AsyncSession=Depends(get_session),todo_repo:ToDoRepository=Depends(get_todo_repository)):
    return ToDoService(session,todo_repo)

