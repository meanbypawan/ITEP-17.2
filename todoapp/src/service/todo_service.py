from src.model import ToDo
from src.repository.todo_repository import ToDORepository


class ToDoService:
    def __init__(self,session):
       self.todo_repo = ToDORepository(session)

    async def save(self,todo:ToDo):
        return await self.todo_repo.save(todo)

    async def get_all_todo(self):
        return await self.todo_repo.get_all_todo()