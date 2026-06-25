from typing import Optional

from fastapi import FastAPI, Request, Form
from sqlalchemy.exc import SQLAlchemyError
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.db.db_config import SessionLocal
from src.model import ToDo

#from starlette.requests import Request

app = FastAPI()
app.mount("/static",StaticFiles(directory="src/static"),name="static")


templates = Jinja2Templates(directory="src/templates")
@app.get("/")
async def home_page(request:Request):
   return templates.TemplateResponse(request,"index.html", {"request": request})

@app.get("/about")
async def about_page(request:Request):
   print(f"Request method : {request.method}")
   print(f"Requested url : {request.url}")
   return templates.TemplateResponse(request,"about.html", {"request": request})

@app.get("/create-to-do")
async def create_to_do_page(request:Request):
   return templates.TemplateResponse(request,"create-to-do.html", {"request": request})


@app.post("/create-to-do")
async def create_to_do(request:Request,
                       title:str=Form(...),
                       description:Optional[str]=Form(None),
                       priority:str=Form(...)):
   try:
      async with SessionLocal.begin() as session:
         todo = ToDo(title=title, description=description, priority=priority)
         session.add(todo)
         return {"message": "ToDo created successfully..."}
   except SQLAlchemyError as e:
      print(e)
      return {"error": "Something went wrong..."}
