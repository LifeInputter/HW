import sqlite3
#
# #можно подключать к БД каждый раз при запросе
# connection = sqlite3.connect('user_log.db')
# cursor = connection.cursor()

# можно написать ф-ю дукоратор для подключения к бд
def get_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('user_log.db') as conn:
            res = func(*args,conn=conn, **kwargs)
        return res
    return inner

# force = true будет пересоздавать таблицы
@get_connection
def init_db(conn,force: bool = False):
    c = conn.cursor()
    if force:
        c.execute("DROP TABLE IF EXISTS user_message")
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_message (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    text TEXT NOT NULL
    )
    ''')
    conn.commit()

@get_connection
def add_message(conn, user_id: int, text: str):
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?,?)', (user_id, text))
    conn.commit()
@get_connection
def count_messages(conn, user_id:int):
    c = conn.cursor()
    c.execute('SELECT COUNT (*) FROM user_message WHERE user_id =?',  (user_id,))
    (res,) = c.fetchone()
    return res

#ф-я для показа последних 5 сообщений из БД по убыванию
@get_connection
def list_messages(conn, user_id: int, limit:int=5):
    c = conn.cursor()
    c.execute('SELECT id, text FROM user_message WHERE user_id = ? ORDER BY id DESC LIMIT?', (user_id, limit))
    return c.fetchall()

if __name__ == "__main__":
    init_db()
#

# r=count_messages(user_id=5482669413)
# print(r)
#
# r = list_messages(user_id=5482669413, limit=5)
# for i in r:
#     print(i)
#
