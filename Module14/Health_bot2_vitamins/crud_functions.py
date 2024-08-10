import os.path
import sqlite3
from Health_bot_2_MoreVitamins import *

DB_FILE_NAME = "prod.db"

connection = sqlite3.connect(DB_FILE_NAME)
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );  
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT TEXT NOT NULL    
    );
    ''')

    connection.commit()
    connection.close()


def add_user(username, email, age, balance=1000):
    if not os.path.exists(DB_FILE_NAME):
        initiate_db()
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'{username}', f'{email}', f'{age}', f'{balance}'))
    connection.commit()
    connection.close()


def is_included(username):
    if not os.path.exists(DB_FILE_NAME):
        initiate_db()
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()

    check = cursor.execute("SELECT username FROM Users WHERE username =?", (username,)).fetchone()
    connection.commit()
    connection.close()
    print(check)
    return check


connection.commit()


# connection.close()


def get_all_products():
    if not os.path.exists(DB_FILE_NAME):
        initiate_db()
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    # connection.close()
    return products
