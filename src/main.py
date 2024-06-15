from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import connect, Error
from pydantic import BaseModel
from typing import List, Dict, Any
from contextlib import contextmanager

app = FastAPI()

class User(BaseModel):
    username: str
    name: str
    password: str

@contextmanager
def get_db_connection():
    try:
        mydb = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Developer1*',
            database='Lagoon_test'
        )
        if mydb.is_connected():
            yield mydb
    except Error as e:
        print(f"Error: {e}")
    finally:
        mydb.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to allow specific origins instead of all
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get("/db")
def get_users():
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        data = transform_query_output(result)
        cursor.close()  # Make sure to close the cursor
        return {"users": data}

def transform_query_output(query_output: List[tuple]) -> Dict[int, Dict[str, Any]]:
    users = {}
    for user in query_output:
        user_id, username, name, password = user
        users[user_id] = {"username": username, "name": name, "password": password}
    return users

# Include other routers
from chat import router as chat_router
from users import router as user_router

app.include_router(chat_router, prefix="/chat")
app.include_router(user_router, prefix="/user")

# Run the app using `uvicorn filename:app --reload` to see the output
