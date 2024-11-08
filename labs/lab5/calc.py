import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
width, height = 400, 650
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Матюхін О. ПКК-31 Калькулятор")

# Визначення кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (169, 169, 169)
GRAY = (200, 200, 200)
PRESSED_COLOR = (150, 150, 150)  # Колір кнопки при натисканні
LIGHT_RED = (255, 182, 193)  # Блідно-червоний для кнопки виходу

# Шрифти
font = pygame.font.Font(None, 36)

# Поле для збереження введення
current_input = ""
result = ""

# Змінна для збереження натиснутої кнопки
pressed_button = None

# Функція для обробки подій кнопок
def handle_button(value):
    global current_input, result
    if value == "=":
        try:
            result_value = eval(current_input)
            if result_value == int(result_value):
                result = str(int(result_value))  # Якщо ціле, то перетворюємо на int і до str
            else:
                result = str(result_value)  # Інакше залишаємо з плаваючою точкою
        except Exception as e:
            result = "Помилка"
    elif value == "C":
        current_input = ""
        result = ""
    elif value == "⌫":
        current_input = current_input[:-1]  # Видалення останнього символу
    else:
        current_input += value

# Створення кнопок ітерацій з числами
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

# Додати кнопку виходу
exit_button_rect = pygame.Rect(200, height - 100, width - 200, 100)  # Розміщення в правому нижньому кутку

# Основний цикл
running = True
while running:
    window.fill(WHITE)

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
        pygame.draw.rect(window, DARK_GRAY, rect, 1,4)
        button_text = font.render(text, True, BLACK)
        text_rect = button_text.get_rect(center=rect.center)
        window.blit(button_text, text_rect)

    # Малювання кнопки виходу
    pygame.draw.rect(window, LIGHT_RED, exit_button_rect)  # Колір фону
    pygame.draw.rect(window, DARK_GRAY, exit_button_rect, 1,4)  # Контур
    exit_text = font.render("Вихід", True, BLACK)
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
    window.blit(exit_text, exit_text_rect)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for text, rect in button_rects:
                if rect.collidepoint(event.pos):
                    pressed_button = rect
                    handle_button(text)
            if exit_button_rect.collidepoint(event.pos):
                running = False  # Завершення програми при натисканні "Вихід"
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed_button = None

    pygame.display.flip()

pygame.quit()
sys.exit()
