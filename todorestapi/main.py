from fastapi import FastAPI, Depends
from sqlalchemy.exc import SQLAlchemyError

from src.exception.global_exception_handler import resource_not_found_exception_handler, sqlalchemy_error_handler, \
    unkown_exception_handler
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.routes.todo_router import router as todo_router
from src.routes.admin_router import router as admin_router
# app is fastapi application instance
app = FastAPI()

app.add_exception_handler(ResourceNotFoundException,resource_not_found_exception_handler)
app.add_exception_handler(SQLAlchemyError,sqlalchemy_error_handler)
app.add_exception_handler(Exception,unkown_exception_handler)

app.include_router(todo_router)
app.include_router(admin_router)






