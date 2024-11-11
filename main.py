import sqlite3



connection = sqlite3.connect('not_telegram_.db')
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

# ----------------- Добавление информации в базу данных ------------
# for i in range(10):
#     i = i + 1
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{10*i}', '1000'))

# ----------------- Изменение данных в базе данных -----------------
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500 , f'User{i}'))

# ----------------- Удаление данных из БД -------------------------
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}', ))

# ----------------- Сортировка данных в БД ------------------------
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
#
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя:{user[0]} | Почта:{user[1]} | Возраст:{user[2]} | Баланс:{user[3]}')

# ---------------- Удаление определённой строки из БД --------------
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# ---------------- Подсчёт количества записей в БД -----------------
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
# print(total)
# ---------------- Подсчёт суммы балансов в БД -----------------
cursor.execute('SELECT SUM(balance) FROM Users')
total2 = cursor.fetchone()[0]
# print(total2)
# ---------------- Средний баланс пользователей в БД -----------------
cursor.execute('SELECT AVG(balance) FROM Users')
total3 = cursor.fetchone()[0]
# print(total3) # средняя сумма через встроенную функцию
print(total2/total) # средняя сумма через вычисление по предыдущим итогам



connection.commit()
connection.close()