from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    name:str
    email:EmailStr
    password:str
    contact:int

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    contact:str
    token:str