from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Author
from src.repository.author_repository import AuthorRepository


class AuthorService:
    def __init__(self,session):
        self.author_repo = AuthorRepository(session)

    async def create_author(self,author:Author):
        return await self.author_repo.create_author(author)

    async def fetch_all_author(self):
        return await self.author_repo.fetch_all_author()

    async def fetch_author_by_id(self,author_id:int):
      author = await self.author_repo.fetch_author_by_id(author_id)
      if not author:
          raise ResourceNotFoundException("Author not found")
      return author
