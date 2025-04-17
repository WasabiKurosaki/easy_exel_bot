import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('parsed_exel.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Exeldata (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
url TEXT NOT NULL,
xpath TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()