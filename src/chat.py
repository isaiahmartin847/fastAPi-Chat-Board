from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

chat_db = {
    0 : {"text": "first chat", "user" : "isaiah"}
}


class Chat(BaseModel):
    text: str
    user: str
    id: int


@router.get("/chats")
def show_chats() -> dict:
    return chat_db


@router.put("/chat/create")
def create_chat(chat: Chat):
    if chat.id in chat_db:
          raise HTTPException(status_code=409, detail="chat id already exist you can not rewrite over a chat")
    else:
        chat_db[chat.id] = {"user": chat.user, "text": chat.text}
        return {"user": chat.user, "text": chat.text, "text id": chat.id}
    

@router.delete("/chat/delete/{chat_id}")
def delete_chat(chat_id: int):
    if chat_id in chat_db:
        print("item was in the db")
        del chat_db[chat_id]
    else:
        raise HTTPException(status_code=204, detail=f"chat with id of {chat_id} unable to delete chat")

    return {"id": chat_id}


