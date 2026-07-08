from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException

from src.db.db_config import get_session
from src.repository.admin_repository import AdminRepository
from src.repository.todo_repository import ToDoRepository
from src.service.admin_service import AdminService
from src.service.todo_service import ToDoService
from src.utils.jwt_util import verify_token

security = HTTPBearer()

def authenticate(header: HTTPAuthorizationCredentials = Depends(security)):
    token = header.credentials
    if not token:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    payload = verify_token(token)
    return payload

def get_todo_repository(session:AsyncSession=Depends(get_session)):
    return ToDoRepository(session)

def get_todo_service(session:AsyncSession=Depends(get_session),todo_repo:ToDoRepository=Depends(get_todo_repository)):
    return ToDoService(session,todo_repo)

def get_admin_respository(session:AsyncSession=Depends(get_session)):
    return AdminRepository(session)

def get_admin_service(admin_repo:AdminRepository=Depends(get_admin_respository)):
    return AdminService(admin_repo)


