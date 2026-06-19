import asyncio

from sqlalchemy.exc import SQLAlchemyError

from src.db.db_config import SessionLocal
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Author, author
from src.service.author_service import AuthorService

async def fetch_all_author():
    try:
        async  with SessionLocal() as session:
            author_service = AuthorService(session)
            author_list = await author_service.fetch_all_author()
            for author in author_list:
                print(f"{author.id}:{author.name}:{author.email}:{author.country}")
    except SQLAlchemyError as e:
        print(e)
async def create_author():
  try:
    name = input("Enter author name: ")
    email = input("Enter author email: ")
    country = input("Enter author country: ")
    async with SessionLocal.begin() as session:
       author = Author(name=name, email=email, country=country)
       author_service = AuthorService(session)
       author = await author_service.create_author(author)
       await session.refresh(author)
       print(f"{author.id}:{author.name}:{author.email}:{author.country}")

  except SQLAlchemyError as e:
      print(e)

async def fetch_author_by_id():
    try:
        async with SessionLocal() as session:
             author_service = AuthorService(session)
             id = int(input("Enter author id: "))
             author = await author_service.fetch_author_by_id(id)
             print(f"{author.id}:{author.name}:{author.email}:{author.country}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def main():
    while True:
        print("1 for creating author")
        print("2 for fetching all author")
        print("3 for fetching author by id")
        print("0 for exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            await create_author()
        elif choice == 0:
            break
        elif choice == 2:
            await fetch_all_author()
        elif choice == 3:
            await fetch_author_by_id()
asyncio.run(main())