from src.model import ToDo


class ToDoRepository:
    def __init__(self,session):
        self.session = session

    async def create(self,todo:ToDo):
        self.session.add(todo)
        await self.session.flush()
        await self.session.refresh(todo)
        return todo