from fastapi import FastAPI
from chat import router as chat_router 
from users import router as user_router

app = FastAPI()

app.include_router(chat_router, prefix="/chat")
app.include_router(user_router, prefix="/user")

