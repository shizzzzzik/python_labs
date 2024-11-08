import requests
import json

def fetch_and_save_posts(url, filename):
    try:
        # Виконання GET-запиту
        response = requests.get(url)
        
        # Перевірка, чи успішно виконано запит
        if response.status_code == 200:
            # Отримуємо дані у форматі JSON
            posts = response.json()

            # Записуємо дані у файл
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(posts, f, ensure_ascii=False, indent=4)

            print(f"Дані успішно збережено у файл {filename}")
        else:
            print(f"Не вдалося отримати дані. Статус код: {response.status_code}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# URL API сервісу JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Виклик функції для отримання та збереження даних
fetch_and_save_posts(url, 'posts.json')
