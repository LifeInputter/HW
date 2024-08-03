import sqlite3

connection = sqlite3.connect('prod.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT TEXT NOT NULL    
    );
    ''')
    connection.commit()



def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products



