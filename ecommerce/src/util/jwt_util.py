from fastapi import HTTPException
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

from starlette import status

load_dotenv()
def generate_token(payload:dict):
    SECRET_KEY = os.getenv("TOKEN_SECRET")
    return jwt.encode(claims=payload,key=SECRET_KEY,algorithm="HS256")

def verify_token(token:str):
   try:
    payload = jwt.decode(token,key=os.getenv("TOKEN_SECRET"),algorithms="HS256")
    return payload
   except JWTError as err:
       print(err)
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token is expired or invalid")
