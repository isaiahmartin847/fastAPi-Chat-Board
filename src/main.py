from fastapi import FastAPI
from chat import router as chat_router 
from users import router as user_router
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector 
from mysql.connector.errors import Error



app = FastAPI()

try: 
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Developer1*',
        database='Lagoon_test'  # Replace with your database name or remove if not connecting to a specific database
    )

    if connection.is_connected():
        print("Connected to MySQL database")


except Error as e:
    print(f"Error: {e}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to allow specific origins instead of all
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(chat_router, prefix="/chat")
app.include_router(user_router, prefix="/user")

