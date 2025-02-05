import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Переход в полноэкранный режим
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Определяем 10 разных цветов
colors = [
    (255, 0, 0),      # Красный
    (0, 255, 0),      # Зеленый
    (0, 0, 255),      # Синий
    (255, 255, 0),    # Желтый
    (0, 255, 255),    # Голубой
    (255, 0, 255),    # Магента
    (192, 192, 192),  # Серый
    (128, 0, 0),      # Темно-красный
    (0, 128, 0),      # Темно-зеленый
    (0, 0, 128)       # Темно-синий
]

# Основной цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Мигать цветами
    for color in colors:
        screen.fill(color)
        pygame.display.flip()
        time.sleep(0.5)  # Задержка в 0.5 секунды

# Закрыть Pygame
pygame.quit()


