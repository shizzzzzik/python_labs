import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Видалення запису
cursor.execute('''
DELETE FROM Students
WHERE name = ?
''', ('Марія',))

# Зберігаємо зміни
conn.commit()

print("Запис видалено успішно!")

# Закриття з'єднання
conn.close()

print("З'єднання завершено")