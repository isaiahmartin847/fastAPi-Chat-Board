from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from testDB import users_db, chat_db


router = APIRouter()

count = 0

def increment_count():
    global count 
    count += 1

class Chat(BaseModel):
    text: str
    username: str
    # id: int


@router.get("/")
def show_chats() -> dict:
    return chat_db


@router.post("/create")
def create_chat(chat: Chat):
    # if chat.id in chat_db:
    #       raise HTTPException(status_code=409, detail="chat id already exist you can not rewrite over a chat")
    
    if chat.username not in users_db:
        raise HTTPException(status_code=409, detail=f"user with username of {chat.username} does not exist")
    
    increment_count()


    chat_db[count] = {"username": chat.username, "text": chat.text}
    return {"username": chat.username, "text": chat.text}
    

@router.delete("/delete/{chat_id}")
def delete_chat(chat_id: int):
    if chat_id in chat_db:
        del chat_db[chat_id]
    else:
        raise HTTPException(status_code=204, detail=f"chat with id of {chat_id} unable to delete chat")

    return {"id": chat_id}



