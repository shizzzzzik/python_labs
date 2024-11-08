def processfile(input_filename, output_filename):
    # Створюємо обробник подій
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            # Отримання рядків у файлі
            lines = infile.readlines()

        # Отримання кількості рядків та виведення їх у термінал
        line_count = len(lines)
        print(f"Кількість рядків у файлі: {line_count}")

        # Створення списку для збереження результатів
        results = []
        
        # Обробляємо кожен рядок
        for i, line in enumerate(lines, start=1):
            # Підраховуємо кількість слів у рядку
            word_count = len(line.split())
            results.append(f"Рядок {i}: {line.strip()} (Кількість слів: {word_count})\n")

        # Записуємо результати у новий файл
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            # Спочатку записуємо кількість рядків
            outfile.write(f"Кількість рядків у файлі: {line_count}\n\n")
            # Потім записуємо кожен рядок з кількістю слів
            outfile.writelines(results)
        
        print(f"Результати записані у файл {output_filename}.")

    except FileNotFoundError:
        print(f"Помилка: файл {input_filename} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Введення користувачем назви файлів для читання та запису
input_filename = input("Введіть ім'я вхідного файлу (з розширенням): ")
output_filename = 'results.txt'

processfile(input_filename, output_filename)