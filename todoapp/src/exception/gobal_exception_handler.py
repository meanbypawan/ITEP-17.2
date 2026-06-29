from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from src.exception.resouce_not_found_exception import ResourceNotFoundException

templates = Jinja2Templates(directory="src/templates")
def resouce_not_found_exception_handler(request:Request,exc:ResourceNotFoundException):
    return templates.TemplateResponse(request,"error.html",{
        "request":request,
        "exc":exc.message
    })

def sqlalchemy_exception_handler(request:Request,exc:SQLAlchemyError):
    print(exc)
    return templates.TemplateResponse(request,"error.html",{
        "request":request,
        "exc":str(exc)
    })
def global_exception(request:Request,exc:Exception):
    return templates.TemplateResponse(request,"error.html",{
        "request":request,
        "exc":str(exc)
    })



