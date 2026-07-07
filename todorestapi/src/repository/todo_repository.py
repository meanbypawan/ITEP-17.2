from sqlalchemy import select

from src.model import ToDo


class ToDoRepository:
    def __init__(self,session):
        self.session = session

    async def create(self,todo:ToDo):
        self.session.add(todo)
        await self.session.flush()
        await self.session.refresh(todo)
        return todo

    async def fetch_all(self):
        statement = select(ToDo)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def fetch_todo_by_id(self,id:int):
        return await self.session.get(ToDo,id)

    async def fetch_todo_by_priority(self,priority:str):
        # select * from todo where priority =: priority
        statement = select(ToDo).where(ToDo.priority==priority)
        result = await self.session.execute(statement)
        return result.scalars().all()
