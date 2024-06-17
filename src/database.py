from mysql.connector import connect, Error
import mysql.connector



def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="developer",
        password="Developer1*",
        database="Lagoon_test"
    )
    return mydb
