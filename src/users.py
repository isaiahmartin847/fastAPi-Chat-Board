from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# from testDB import users_db, chat_db
from database import get_db_connection

router = APIRouter()

class UserBase(BaseModel):
    username: str
    name: str
    password: str



@router.get("/users")
def get_users():
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        data = transform_query_output(result)
    return {"users": data}



@router.post("/user/create")
def create_user(user: UserBase): 
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        val = (user.username, user.name, user.password)
        cursor.execute(sql, val)
        mydb.commit()
    return {"message": "user created in the db"}



@router.delete("/user/delete/{id}")
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
