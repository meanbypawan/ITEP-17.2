from sqlalchemy.exc import SQLAlchemyError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.exception.resource_not_found_exception import ResourceNotFoundException


def resource_not_found_exception_handler(request:Request,exc:ResourceNotFoundException):
   print("Resouce not fund exception handler called...")
   return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                       content={
                           "message":exc.message
                       })

def sqlalchemy_error_handler(request:Request,exc:SQLAlchemyError):
    print("SQLAlchemy error handler called...",exc)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={
                            "error":"Database Error"
                        })

def unkown_exception_handler(request:Request,exc:Exception):
    print("Internal exception handler called...",exc)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={
                            "error":"Internal Server Error"
                        })

