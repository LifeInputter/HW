import sqlite3

connection = sqlite3.connect('not_telegramm.db')  # подключаем файл бд
cursor = connection.cursor()  # аналог мыши, необходим для навигации и выбора элементов бд

# создание таблицы Users с использованием осн.команд на языке SQL
# команды пишем ЗАГЛАВНЫМИ буквами(капсом), названия таблиц пишшутся с Большой быквы, названия столбцов - малленьким шрифтом

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(       
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email On Users (email)")  # создание индекса на email

# добавление в определенные поля БД значений (INSERT INTO)
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500
for i in range(1, 11):
    if i % 2 != 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ("500", f'{i}'))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
for j in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username =?", (f'User{j}',))

#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль
#в следующем формате (без id): Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

cursor.execute("SELECT username, email, age, balance  FROM Users WHERE age !=?", (60,))
# cursor.execute("SELECT username FROM Users WHERE age !=?", (60,))
users = cursor.fetchall()

for user in users:
    username, email, age, balance = user
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()  # позоляет сохранить состояние
connection.close()  #закрытие
