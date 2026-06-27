from typing import Optional

from fastapi import FastAPI, Request, Form
from sqlalchemy.exc import SQLAlchemyError
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.db.db_config import SessionLocal
from src.model import ToDo
from src.service.todo_service import ToDoService

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
async def create_to_do_page(request:Request,message:Optional[str]=None):
   return templates.TemplateResponse(request,"create-to-do.html", {"request": request,"message":message})


@app.post("/create-to-do")
async def create_to_do(request:Request,
                       title:str=Form(...),
                       description:Optional[str]=Form(None),
                       priority:str=Form(...)):
   try:
      async with SessionLocal.begin() as session:
         todo = ToDo(title=title, description=description, priority=priority)
         todo_service = ToDoService(session)
         todo = await todo_service.save(todo)
         #return templates.TemplateResponse(request,"create-to-do.html",{"request":request})
         return RedirectResponse("/create-to-do?message=To do created successfully..",status_code=303)# GET
   except SQLAlchemyError as e:
      print(e)
      return {"error": "Something went wrong..."}

@app.get("/to-do-list")
async def get_to_do_list(request:Request):
   try:
      async with SessionLocal() as session:
         todo_service = ToDoService(session)
         todo_list  = await todo_service.get_all_todo()
         print(todo_list)
         return templates.TemplateResponse(request,"todo-list.html",{"request": request,"todo_list":todo_list})
   except SQLAlchemyError as e:
      print(e)

@app.get("/delete-to-do/{id}")
async def delete_todo(request:Request,id:int):
   pass






