from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_db_connection
from typing import List, Dict, Any
# from testDB import users_db, chat_db


router = APIRouter()


class ChatBase(BaseModel):
    text: str
    user: int


def convert_to_dict_list(data):
    result = []
    for item in data:
        user_message_dict = {
            "user": item[2],
            "message": item[1]
        }
        result.append(user_message_dict)
    return result


@router.get("/")
def get_users():
    query = """
SELECT messages.message_id, messages.text, users.username
FROM messages
JOIN users ON messages.user_id = users.id
ORDER BY messages.message_id
    """
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        data = convert_to_dict_list(result)
    return {"messages": data}


@router.post("/create")
def create_chat(chat: ChatBase):
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        sql = "INSERT INTO messages (text, user_id) VALUES (%s, %s)"
        val = (chat.text, chat.user)
        cursor.execute(sql, val)
        mydb.commit()
    return {"message": "message created"}


    

@router.delete("/delete/{chat_id}")
def delete_chat(chat_id: int):
    with get_db_connection() as mydb:
        cursor = mydb.cursor()
        cursor.execute(f"DELETE FROM messages WHERE message_id = {chat_id}")
        mydb.commit()

    return {"message": f"deleted the message {chat_id}"}



