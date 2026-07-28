from jose import jwt
from dotenv import load_dotenv
import os
load_dotenv()
def generate_token(payload:dict):
    SECRET_KEY = os.getenv("TOKEN_SECRET")
    return jwt.encode(claims=payload,key=SECRET_KEY,algorithm="HS256")