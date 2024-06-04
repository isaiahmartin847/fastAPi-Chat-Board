from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Users(BaseModel):
    name: str
    username: str
    email: str

users_db = {
    "johnDoe": {"name": "John", "email" : "johndoe@example.com"}
}


@router.get("/")
def show_users() -> dict:
    return users_db

@router.post("/create")
def create_user(user: Users) -> dict:
    if user.username in users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    
    users_db[user.username] = {"name": user.name, "email": user.email}
    return {"Name": user.name, "email": user.email}



@router.delete("/delete/{user_name}")
async def delete_user(user_id: str) -> int:
    return(user_id)