import pygame
import sys
import json
import os

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
width, height = 400, 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Матюхін О. ПКК-31 Калькулятор")

# Визначення кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (169, 169, 169)
GRAY = (200, 200, 200)
PRESSED_COLOR = (150, 150, 150)
LIGHT_RED = (255, 182, 193)
LIGHT_GREEN = (144, 238, 144)

# Шрифти
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Поле для збереження введення
current_input = ""
result = ""
last_was_number = False
last_was_operator = False
last_was_minus = False
show_history = False
current_page = 0
items_per_page = 5

# Шлях до JSON-файлу для збереження історії
history_file = "history.json"

# Змінна для збереження натиснутої кнопки
pressed_button = None

# Функція для збереження виразів у JSON
def save_to_json(expression, result):
    history = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = json.load(file)
    history.append({"expression": expression, "result": result})
    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

# Функція для зчитування історії
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            return json.load(file)
    return []

# Функція для обробки подій кнопок
def handle_button(value):
    global current_input, result, last_was_number, last_was_operator, last_was_minus, show_history, current_page
    if value in "0123456789":
        current_input += value
        last_was_number = True
        last_was_operator = False
        last_was_minus = False
    elif value == ".":
        last_number_part = current_input.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]
        if "." not in last_number_part:
            if not current_input or current_input[-1] in "+-*/":
                current_input += "0"
            current_input += value
            last_was_number = False
            last_was_operator = False
            last_was_minus = False
    elif value == "-" and not last_was_minus and (not current_input or current_input[-1] in "+-*/"):
        current_input += value
        last_was_number = False
        last_was_operator = False
        last_was_minus = True
    elif value in "+-*/" and last_was_number:
        current_input += value
        last_was_number = False
        last_was_operator = True
        last_was_minus = False
    elif value == "=" and last_was_number:
        if current_input == "-" or current_input == "":
            return
        try:
            result_value = eval(current_input)
            if result_value == int(result_value):
                result = str(int(result_value))
            else:
                result = str(result_value)
            save_to_json(current_input, result)
        except Exception as e:
            result = "Помилка"
        current_input = ""
        last_was_number = False
        last_was_operator = False
        last_was_minus = False
    elif value == "C":
        current_input = ""
        result = ""
        last_was_number = False
        last_was_operator = False
        last_was_minus = False
    elif value == "⌫":
        current_input = current_input[:-1]
        if current_input:
            last_was_number = current_input[-1].isdigit()
            last_was_operator = current_input[-1] in "+-*/"
            last_was_minus = current_input[-1] == "-"
        else:
            last_was_number = False
            last_was_operator = False
            last_was_minus = False
    elif value == "Історія":
        show_history = not show_history
        current_page = 0

# Створення кнопок
buttons = [
    "C", "⌫", "/", "=",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", "."
]

button_rects = []
for i, text in enumerate(buttons):
    x = (i % 4) * 100
    y = 150 + (i // 4) * 100
    button_rects.append((text, pygame.Rect(x, y, 100, 100)))

# Додати кнопку виходу та історії
history_button_rect = pygame.Rect(200, height - 150, 200, 100)
exit_button_rect = pygame.Rect(0, height - 50, width, 50)
back_button_rect = pygame.Rect(0, height - 50, width, 50)  # Кнопка повернення на калькулятор
next_button_rect = pygame.Rect(width - 200, height - 100, width - 200, 50)
prev_button_rect = pygame.Rect(0, height - 100, width - 200, 50)

# Основний цикл
running = True
while running:
    window.fill(WHITE)

    if show_history:
        # Показ історії
        history = load_history()
        start_index = current_page * items_per_page
        end_index = min(start_index + items_per_page, len(history))
        for i, item in enumerate(history[start_index:end_index]):
            text = f"{item['expression']} = {item['result']}"
            history_item_text = small_font.render(text, True, BLACK)
            window.blit(history_item_text, (10, 160 + i * 30))

        # Показати кнопки пагінації з блокуванням, якщо немає відповідної сторінки
        if current_page > 0:
            pygame.draw.rect(window, GRAY, prev_button_rect)
            pygame.draw.rect(window, DARK_GRAY, prev_button_rect, 1,4)
            prev_text = small_font.render("Назад", True, BLACK)
            prev_text_rect = prev_text.get_rect(center=prev_button_rect.center)
            window.blit(prev_text, prev_text_rect)
        if end_index < len(history):
            pygame.draw.rect(window, GRAY, next_button_rect)
            pygame.draw.rect(window, DARK_GRAY, next_button_rect, 1,4)
            next_text = small_font.render("Вперед", True, BLACK)
            next_text_rect = next_text.get_rect(center=next_button_rect.center)
            window.blit(next_text, next_text_rect)

        # Кнопка повернення на калькулятор
        pygame.draw.rect(window, LIGHT_GREEN, back_button_rect)
        back_text = font.render("Повернутись до калькулятора", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        window.blit(back_text, back_text_rect)
    else:
        # Виведення поточного введення та результату
        input_text = font.render(current_input, True, BLACK)
        result_text = font.render(result, True, BLACK)
        window.blit(input_text, (10, 10))
        window.blit(result_text, (10, 50))

        # Малювання кнопок
        for text, rect in button_rects:
            if pressed_button == rect:
                pygame.draw.rect(window, PRESSED_COLOR, rect)
            else:
                pygame.draw.rect(window, GRAY, rect)
            pygame.draw.rect(window, DARK_GRAY, rect, 1, 4)
            button_text = font.render(text, True, BLACK)
            text_rect = button_text.get_rect(center=rect.center)
            window.blit(button_text, text_rect)

        # Малювання кнопки виходу
        pygame.draw.rect(window, LIGHT_RED, exit_button_rect)
        pygame.draw.rect(window, DARK_GRAY, exit_button_rect, 1, 4)
        exit_text = font.render("Вихід", True, BLACK)
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        window.blit(exit_text, exit_text_rect)

        # Малювання кнопки історії
        pygame.draw.rect(window, LIGHT_GREEN, history_button_rect)
        pygame.draw.rect(window, DARK_GRAY, history_button_rect, 1,4)
        history_text = font.render("Історія", True, BLACK)
        history_text_rect = history_text.get_rect(center=history_button_rect.center)
        window.blit(history_text, history_text_rect)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_history:
                # Обробка натискань у режимі історії
                if back_button_rect.collidepoint(event.pos):
                    show_history = False
                elif current_page > 0 and prev_button_rect.collidepoint(event.pos):
                    current_page -= 1
                elif end_index < len(history) and next_button_rect.collidepoint(event.pos):
                    current_page += 1
            else:
                # Обробка натискань у режимі калькулятора
                for text, rect in button_rects:
                    if rect.collidepoint(event.pos):
                        pressed_button = rect
                        handle_button(text)
                if exit_button_rect.collidepoint(event.pos):
                    running = False
                elif history_button_rect.collidepoint(event.pos):
                    handle_button("Історія")
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed_button = None

    pygame.display.flip()

pygame.quit()
sys.exit()
