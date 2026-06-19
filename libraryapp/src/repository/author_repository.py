from sqlalchemy import select

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Author

class AuthorRepository:
    def __init__(self,session):
      self.session = session

    async def create_author(self,author:Author):
        self.session.add(author) # insert operation is pending
        await self.session.flush() # it will execute pending operations
        return author

    async def fetch_all_author(self):
        statement = select(Author)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def fetch_author_by_id(self,author_id:int):
        return await self.session.get(Author,author_id)



