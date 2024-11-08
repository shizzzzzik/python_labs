import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Додавання записів до таблиці Students
cursor.execute('''
INSERT INTO Students (name, age, grade)
VALUES (?, ?, ?)
''', ('Іван', 20, 'A'))

cursor.execute('''
INSERT INTO Students (name, age, grade)
VALUES (?, ?, ?)
''', ('Марія', 22, 'B'))

cursor.execute('''
INSERT INTO Students (name, age, grade)
VALUES (?, ?, ?)
''', ('Олександр', 21, 'C'))

# Зберігаємо зміни
conn.commit()

print("Дані додано успішно!")

# Закриття з'єднання
conn.close()

print("З'єднання завершено")