from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    name:str
    email:EmailStr
    password:str
    contact:int