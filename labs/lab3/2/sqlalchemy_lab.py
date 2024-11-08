from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Налаштування бази даних (в даному випадку SQLite)
DATABASE_URL = "sqlite:///students.db"  # Використовуємо SQLite базу даних

# Створюємо базовий клас для всіх моделей
Base = declarative_base()

# Описуємо модель Student для таблиці Students
class Student(Base):
    __tablename__ = 'students'  # Назва таблиці

    # Опис стовпців таблиці
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)

    # Для зручності, визначимо метод __repr__ для виведення об'єктів студентів
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, grade='{self.grade}')>"

# Створення бази даних
engine = create_engine(DATABASE_URL)

# Створення таблиці в базі даних (якщо вона ще не існує)
Base.metadata.create_all(engine)

# Створення сесії для виконання запитів
Session = sessionmaker(bind=engine)
session = Session()

# Додавання кількох записів до таблиці
def add_students():
    # Створюємо об'єкти студентів
    student1 = Student(name='Іван', age=20, grade='A')
    student2 = Student(name='Марія', age=22, grade='B')
    student3 = Student(name='Олександр', age=21, grade='C')

    # Додаємо студентів до сесії
    session.add_all([student1, student2, student3])

    # Підтверджуємо зміни в базі даних
    session.commit()
    print("Дані студентів додано в базу даних.")

# Отримання та виведення всіх записів
def get_students():
    students = session.query(Student).all()  # Отримуємо всі записи з таблиці students
    for student in students:
        print(student)

# Додавання студентів (перший запуск)
add_students()

# Отримуємо та виводимо всі записи
print("Список студентів:")
get_students()

# Закриваємо сесію після виконання операцій
session.close()