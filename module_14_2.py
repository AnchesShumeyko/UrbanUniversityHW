import sqlite3

connection = sqlite3.connect("not_telegram2.db")
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

# Удаление пользователя с id = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Считаем количество пользователей, общий баланс и выводим средний баланс в консоль
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchone()[0]
print(balance_sum / total_users)

connection.commit()
connection.close()
