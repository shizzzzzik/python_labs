import sqlite3

# Створюємо базу даних
conn = sqlite3.connect('database.db')

# Створюємо об'єкт курсора для виконання SQL запитів
cursor = conn.cursor()

# Створення таблиці Students
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

# Зберігаємо зміни
conn.commit()

print("Таблиця створена успішно!")

# Закриття з'єднання
conn.close()

print("З'єднання завершено")