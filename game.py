import pygame
import random
from db import db

pygame.init()

# Инициализация экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("спасись от куба")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Параметры квадрата
square_size = 50
square_x = screen_width // 2
square_y = screen_height - square_size
score = 0

# Параметры мячей
ball_radius = 15
ball_y = 0
ball_x = random.randint(0, screen_width - ball_radius)

# Параметры зеленого круга
green_ball_radius = 15
green_ball_y = random.randint(0, screen_height // 2)
green_ball_x = random.randint(0, screen_width - green_ball_radius)

scores = db.select()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if score not in [s[0] for s in scores]:
                db.insert(score)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and square_x > 0:
        square_x -= 10
    if keys[pygame.K_d] and square_x < screen_width - square_size:
        square_x += 10
    if keys[pygame.K_w] and square_y > 0:
        square_y -= 10
    if keys[pygame.K_s] and square_y < screen_height - square_size:
        square_y += 10

    # Движение мяча
    ball_y += 8
    if ball_y > screen_height:
        ball_y = 0
        ball_x = random.randint(0, screen_width - ball_radius)
    if (square_x < ball_x < square_x + square_size) and (square_y < ball_y < square_y + square_size):
        score += 5
        ball_y = 0
        ball_x = random.randint(0, screen_width - ball_radius)

    # Движение зеленого мяча
    green_ball_y += 8
    if green_ball_y > screen_height:
        green_ball_y = 0
        green_ball_x = random.randint(0, screen_width - green_ball_radius)
    if (square_x < green_ball_x < square_x + square_size) and (square_y < green_ball_y < square_y + square_size):
        # Сбросить игру и сбросить рекорд
        db.insert(score)
        score = 0
        green_ball_y = random.randint(0, screen_height // 2)
        green_ball_x = random.randint(0, screen_width - green_ball_radius)
    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.circle(screen, GREEN, (green_ball_x, green_ball_y), green_ball_radius)

    # Отображение счета
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    for i in range(len(scores)):
        score_text = font.render(f"Score: {scores[i][0]}", True, (0, 0, 0))
        screen.blit(score_text, (screen_width - 150, i * 30))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()



