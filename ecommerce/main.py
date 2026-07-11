from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from starlette.staticfiles import StaticFiles

from src.exception import resource_not_found_exception
from src.exception.global_exception_handler import sqlalchemy_error_handler, resource_not_found_exception_handler, \
    unkown_exception_handler
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.router.user_router import router as user_router
from src.router.category_router import router as category_router
app = FastAPI()
app.add_exception_handler(SQLAlchemyError,sqlalchemy_error_handler)
app.add_exception_handler(ResourceNotFoundException,resource_not_found_exception_handler)
app.add_exception_handler(Exception,unkown_exception_handler)

app.mount("/public",StaticFiles(directory="src/public"),name="public")

# http://localhost:8000/user
app.include_router(user_router)
app.include_router(category_router)