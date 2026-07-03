from src.model import ToDo
from src.repository.todo_repository import ToDoRepository
from src.schema.todo_schema import ToDoRequest


class ToDoService:
    def __init__(self,session):
        self.session = session
        self.todo_repo = ToDoRepository(session)

    async def create(self,request:ToDoRequest):
        todo = ToDo(title = request.title,description=request.description,priority = request.priority)
        return await self.todo_repo.create(todo)