import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# заполнение таблицы
for i in range(10):
    sql_request = "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)"
    params = (f'user{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1) * 10}', 1000)
    cursor.execute(sql_request, params)

# изменение баланса у каждой второй записи с 1ой на 500:
counter = 1
while counter <= 10:
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, counter))
    counter += 2

# удаление каждого третьего пользователя, начиная с первого
counter_2 = 1
while counter_2 <= 10:
    cursor.execute('DELETE FROM Users WHERE id = ?', (counter_2,))
    counter_2 += 3

# выбор пользователей с возрастом неравным 60 и вывод в консоль имени, почты, возраста и баланса
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
