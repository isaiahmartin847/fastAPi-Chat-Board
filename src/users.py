from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_db_connection
from typing import List, Dict, Any

router = APIRouter()

class UserBase(BaseModel):
    username: str
    name: str
    password: str



@router.get("/")
def get_users():
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        data = transform_query_output(result)
    return {"users": data}



@router.post("/create")
def create_user(user: UserBase): 
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        val = (user.username, user.name, user.password)
        cursor.execute(sql, val)
        mydb.commit()

        user_id = cursor.lastrowid

    return {"user_id": user_id}



@router.delete("/delete/{id}")
def delete_user(id: int):
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = {id}")
        mydb.commit()

    return {"message": f"deleted the user {id}"}



@router.get("/{username}")
def get_user(username: str):
     
    with get_db_connection() as mydb:

        cursor = mydb.cursor()
        cursor.execute(f"SELECT users.password, users.id FROM users Where username = '{username}'")
        result = cursor.fetchall()
    
    if len(result) == 0: 
        raise HTTPException(status_code=404, detail="User not found")
    else :
        # print(result)
        return {"password": result[0][0], "id": result[0][1]}
    
    


def transform_query_output(query_output: List[tuple]) -> Dict[int, Dict[str, Any]]:
    users = {}
    for user in query_output:
        user_id, username, name, password = user
        users[user_id] = {"username": username, "name": name, "password": password}
    return users


