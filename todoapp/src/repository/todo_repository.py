from sqlalchemy import select

from src.model import ToDo


class ToDORepository:
    def __init__(self,session):
        self.session = session

    async def save(self,todo:ToDo):
        self.session.add(todo)
        return todo

    async def get_all_todo(self):
        statement = select(ToDo)
        todo_list = await self.session.execute(statement)
        return todo_list.scalars().all()

    async def get_todo_by_id(self,id:int):
        return await self.session.get(ToDo,id)

    async def delete_todo(self,todo:ToDo):
        return await self.session.delete(todo)
