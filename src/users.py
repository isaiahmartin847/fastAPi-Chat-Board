from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from testDB import users_db, chat_db

router = APIRouter()

class Users(BaseModel):
    name: str
    username: str



@router.get("/")
def show_users() -> dict:
    return users_db

@router.post("/create")
def create_user(user: Users) -> dict:
    if user.username in users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    
    users_db[user.username] = {"name": user.name}
    return {"Name": user.name}



@router.delete("/delete/{user_name}")
def delete_user(user_name: str):
    if user_name not in users_db:
        raise HTTPException(status_code=204, detail=f"user {user_name} does not exist")
    
    del users_db[user_name]
    return(user_name)
