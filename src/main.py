from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import connect, Error
from pydantic import BaseModel
from typing import List, Dict, Any
import mysql.connector


app = FastAPI()

class User(BaseModel):
    username: str
    name: str
    password: str



def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="developer",
        password="Developer1*",
        database="Lagoon_test"
    )
    return mydb



@app.get("/users")
def get_users():
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        data = transform_query_output(result)
    return {"users": data}

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


