from pydantic import BaseModel,EmailStr


class AdminRequest(BaseModel):
    email:EmailStr
    password:str

class AdminResponse(BaseModel):
    id:int
    email:EmailStr
    token:str
