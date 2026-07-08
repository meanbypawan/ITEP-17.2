from jose import jwt, JWTError
from dotenv import load_dotenv
import os

from starlette.exceptions import HTTPException

load_dotenv()
def generate_token(payload:dict):
    token = jwt.encode(claims=payload,
               key=os.getenv("TOKEN_SECRET","trtoitughkfhkghg"),
               algorithm=os.getenv("TOKEN_ALGO","HS256"))
    return token

def verify_token(token:str):
  try:
    payload = jwt.decode(token,
               key=os.getenv("TOKEN_SECRET","trtoitughkfhkghg"),
               algorithms=os.getenv("TOKEN_ALGO","HS256"))
    print(f"Payload : {payload}")
    return payload
  except JWTError as e:
      raise HTTPException(status_code=401,detail="Unauthorized access")
