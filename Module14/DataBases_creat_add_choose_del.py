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


#Удалите из базы данных not_telegram.db запись с id = 6
cursor.execute("DELETE FROM Users WHERE id=?",(6,))

#Подсчитать общее количество записей
cursor.execute("SELECT COUNT (*) FROM Users")
total = cursor.fetchone()[0]
# print(total)

#Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]
# print(total_balance)
print(total_balance/total)  #вариант1

#Вывести в консоль средний баланс всех пользователя
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)                #вариант2


connection.commit()  # позоляет сохранить состояние
connection.close()  #закрытие
