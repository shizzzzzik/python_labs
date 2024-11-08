import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Отримання всіх записів з таблиці
cursor.execute('SELECT * FROM Students')

# Виведення результатів
students = cursor.fetchall()
for student in students:
    print(student)

# Закриття з'єднання
conn.close()

print("З'єднання завершено")