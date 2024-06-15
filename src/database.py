import mysql.connector
from contextlib import contextmanager
from config import DATABASE_CONFIG
from mysql.connector import connect, Error




@contextmanager
def get_db_connection():
    db = None
    try:
        db = connect(**DATABASE_CONFIG)
        if db.is_connected():
            yield db
    except Error as e:
        print(f"Error: {e}")
    finally:
        db.close()
