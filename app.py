from fastapi import FastAPI
import mysql.connector 

app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        port=3306,
        user="appuser",
        password="app123",
        database="appdb"
    )

@app.get("/")
def home():
    return {
        "message": "FastApi + MySQL Docker project",
        "status": "running"
    }

@app.get("/users")
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    connection.close()
    return users