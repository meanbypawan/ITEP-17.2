from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import ToDo
from src.repository.todo_repository import ToDoRepository
from src.schema.todo_schema import ToDoRequest

class ToDoService:
    def __init__(self,session,todo_repo:ToDoRepository):
        self.session = session
        self.todo_repo = todo_repo
    async def create(self,request:ToDoRequest):
        todo = ToDo(title = request.title,description=request.description,priority = request.priority)
        return await self.todo_repo.create(todo)
    async def fetch_all(self):
        return await self.todo_repo.fetch_all()

    async def fetch_todo_by_id(self,id:int):
        todo = await self.todo_repo.fetch_todo_by_id(id)
        if not todo:
            raise ResourceNotFoundException(f"Todo with id {id} not found")
        return todo

    async def fetch_todo_by_priority(self,priority:str):
        return await self.todo_repo.fetch_todo_by_priority(priority)

