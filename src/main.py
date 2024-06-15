from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import connect, Error
from pydantic import BaseModel
from typing import List, Dict, Any
from contextlib import contextmanager
from models import get_all_users
# from database import get_db_connection

app = FastAPI()

class User(BaseModel):
    username: str
    name: str
    password: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to allow specific origins instead of all
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get("/db")
def get_users():



        result = get_all_users()
        data = transform_query_output(result)
          
        return {"users": data}

# def get_users(query: str):
#     with get_db_connection() as mydb:
#         cursor = mydb.cursor()
#         cursor.execute("SELECT * FROM users")
#         result = cursor.fetchall()
#         cursor.close()
#         return result

def transform_query_output(query_output: List[tuple]) -> Dict[int, Dict[str, Any]]:
    users = {}
    for user in query_output:
        user_id, username, name, password = user
        users[user_id] = {"username": username, "name": name, "password": password}
    return users

from chat import router as chat_router
from users import router as user_router

app.include_router(chat_router, prefix="/chat")
app.include_router(user_router, prefix="/user")


