import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Оновлення віку студента
cursor.execute('''
UPDATE Students
SET age = ?
WHERE name = ?
''', (23, 'Іван'))

# Зберігаємо зміни
conn.commit()

print("Дані оновлено успішно!")

# Закриття з'єднання
conn.close()

print("З'єднання завершено")