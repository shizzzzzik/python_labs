# Написання функції для обчислення факторіалу

def factorial(n):
    # Якщо число дорівнює 0 або 1, повертаємо 1 за визначенням факторіалу
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Введення числа факторіалу

num = int(input("Введіть число для обчислення факторіалу: "))

# Перевірка числа факторіалу на від'ємні числа

if num < 0:
    print("Факторіал не існує для від'ємних чисел.")
else:
    print(f"Факторіал числа {num} дорівнює {factorial(num)}")