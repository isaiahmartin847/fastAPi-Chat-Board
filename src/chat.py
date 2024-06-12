from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from users import users_db

router = APIRouter()

chat_db = {
    0 : {"text": "Hello world", "username" : "johnDoe"},

}


class Chat(BaseModel):
    text: str
    username: str
    id: int


@router.get("/")
def show_chats() -> dict:
    return chat_db


@router.post("/create")
def create_chat(chat: Chat):
    if chat.id in chat_db:
          raise HTTPException(status_code=409, detail="chat id already exist you can not rewrite over a chat")
    
    if chat.username not in users_db:
        raise HTTPException(status_code=204, detail=f"user with username of {chat.username} does not exist")
    
    
    chat_db[chat.id] = {"username": chat.username, "text": chat.text}
    return {"username": chat.username, "text": chat.text, "text id": chat.id}
    

@router.delete("/delete/{chat_id}")
def delete_chat(chat_id: int):
    if chat_id in chat_db:
        del chat_db[chat_id]
    else:
        raise HTTPException(status_code=204, detail=f"chat with id of {chat_id} unable to delete chat")

    return {"id": chat_id}



