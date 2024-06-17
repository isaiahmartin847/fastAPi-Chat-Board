from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from database import get_db_connection
# import mysql.connector
# from mysql.connector import connect, Error


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["Content-Type"],
)

class UserBase(BaseModel):
    username: str
    name: str
    password: str






# def get_db_connection():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="developer",
#         password="Developer1*",
#         database="Lagoon_test"
#     )
#     return mydb



@app.get("/users")
def get_users():
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        data = transform_query_output(result)
    return {"users": data}



@app.post("/user/create")
def create_user(user: UserBase): 
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        val = (user.username, user.name, user.password)
        cursor.execute(sql, val)
        mydb.commit()
    return {"message": "user created in the db"}



@app.delete("/user/delete/{id}")
def delete_user(id: int):
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = {id}")
        mydb.commit()

    return {"message": f"deleted the user {id}"}


def transform_query_output(query_output: List[tuple]) -> Dict[int, Dict[str, Any]]:
    users = {}
    for user in query_output:
        user_id, username, name, password = user
        users[user_id] = {"username": username, "name": name, "password": password}
    return users



# from chat import router as chat_router
# from users import router as user_router

# app.include_router(chat_router, prefix="/chat")
# app.include_router(user_router, prefix="/user")


