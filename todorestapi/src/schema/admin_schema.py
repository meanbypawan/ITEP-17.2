from pydantic import BaseModel,EmailStr


class AdminRequest(BaseModel):
    email:EmailStr
    password:str

