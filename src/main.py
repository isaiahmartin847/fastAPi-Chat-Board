from fastapi import FastAPI
from chat import router as chat_router 
from users import router as user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to allow specific origins instead of all
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(chat_router, prefix="/chat")
app.include_router(user_router, prefix="/user")

