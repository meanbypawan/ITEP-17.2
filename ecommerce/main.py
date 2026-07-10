from fastapi import FastAPI
from src.router.user_router import router as user_router
app = FastAPI()

# http://localhost:8000/user
app.include_router(user_router)