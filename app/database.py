import psycopg2
import os
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")


def get_connection():
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE tasks(
            id  INTEGER,
            title  TEXT,
            done  BOOLEAN
    )
       """)
    
    conn.commit()

    print("TABLE CREATED")