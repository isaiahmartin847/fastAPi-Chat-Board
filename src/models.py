from database import get_db_connection
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import connect, Error
from pydantic import BaseModel
from typing import List, Dict, Any
from contextlib import contextmanager



# def get_users():
#     with get_db_connection() as db:
#         cursor = db.cursor()
#         cursor.execute("SELECT * FROM users")
#         result = cursor.fetchall()
#         cursor.close()
#         return result

        


def get_all_users():


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result