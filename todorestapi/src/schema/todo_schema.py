import email
from typing import Optional

from pydantic import BaseModel


class ToDoRequest(BaseModel):
    title:str
    priority:str
    description:Optional[str] = None

class ToDoResponse(BaseModel):
    id:int
    title:str
    description:Optional[str] = None