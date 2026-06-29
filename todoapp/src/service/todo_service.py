from src.exception.resouce_not_found_exception import ResourceNotFoundException
from src.model import ToDo
from src.repository.todo_repository import ToDORepository


class ToDoService:
    def __init__(self,session):
       self.todo_repo = ToDORepository(session)
       self.session = session
    async def save(self,todo:ToDo):
        return await self.todo_repo.save(todo)

    async def get_all_todo(self):
        return await self.todo_repo.get_all_todo()

    async def delete_todo(self,id:int):
           todo = await self.todo_repo.get_todo_by_id(id)
           if not todo:
               raise ResourceNotFoundException(f"Resouce with {id} not found")
           await self.todo_repo.delete_todo(todo)
           return todo

    async def get_todo_by_id(self,id:int):
        todo =  await self.todo_repo.get_todo_by_id(id)
        if not todo:
            raise ResourceNotFoundException(f"Resouce with {id} not found")
        return todo
    async def update_todo(self,todo:ToDo):
        db_todo = await self.todo_repo.get_todo_by_id(todo.id)
        if not db_todo:
            raise ResourceNotFoundException(f"Resouce with {id} not found")
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.priority = todo.priority
        return db_todo