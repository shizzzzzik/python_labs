# Створення функції, яка отримує масив з числами та обчислюує серед них парні завдяки арифметичному оператору %, який вираховує остачу операнда num
def summa_parnyh(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Введення чисел та додавання їх у масив "numbers"
input_str = input("Введіть числа для обчислення всіх парних (через пробіл): ")
numbers = list(map(int, input_str.split()))

# print(numbers) - перевірка на отримання списку чисел в масив

result = summa_parnyh(numbers)
print(f"Сума парних чисел дорівнює: {result}")