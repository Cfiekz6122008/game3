import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
infoObject = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)  # Полноэкранный режим

# Список цветов
colors = [
    (255, 0, 0),  # Красный
    (0, 255, 0),  # Зеленый
    (0, 0, 255),  # Синий
    (255, 255, 0),  # Желтый
    (255, 165, 0),  # Оранжевый
    (128, 0, 128),  # Пурпурный
    (0, 255, 255)  # Голубой
]

# Загрузка фоновой музыки
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # Повторять бесконечно


# Функция генерации кругов
def generate_circles():
    circles = []
    for _ in range(10):
        radius = random.randint(10, 100)
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = random.randint(radius, SCREEN_HEIGHT - radius)
        color = random.choice(colors)
        circles.append((x, y, radius, color))
    return circles


# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    # Генерация фона
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill(background_color)

    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    # Генерация кругов каждые 200-800 миллисекунд
    circles = generate_circles()

    for circle in circles:
        pygame.draw.circle(screen, circle[3], (circle[0], circle[1]), circle[2])

    pygame.display.flip()

    # Ограничение скорости игры
    clock.tick(1)  # Обновление экрана 1 раз в секунду (интервал генерации кругов)
    pygame.time.delay(random.randint(200, 800))  # Задержка между генерациями кругов


