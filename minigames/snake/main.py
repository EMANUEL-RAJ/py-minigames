# --- Importing Packages ---
import sys
import pygame
import random

from config import *

# --- Game Variables ---
running = True
score = 0
snake_head_x = WIN_WIDTH // 2
snake_head_y = WIN_HEIGHT // 2
snake_dir_x = 1
snake_dir_y = 0
snake_body = []
food_x = random.randint(1, WIN_WIDTH - FOOD_SIZE)
food_y = random.randint(1, WIN_HEIGHT - FOOD_SIZE)


# --- Initializing Pygame and Setting Clock---
pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

# --- Building In-Game Assets ---
# game font
font = pygame.font.SysFont("freesansbold", 15)
score_txt = font.render("Score: " + str(score), True, SCORE_COLOR)
score_rect = score_txt.get_rect(topleft=SCORE_RECT)
# snake
snake_head_coord = (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE)
snake_head_rect = pygame.draw.rect(WIN, SNAKE_COLOR, snake_head_coord)
# food
food_rect = pygame.draw.rect(WIN, FOOD_COLOR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

# --- Main Game Loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and snake_dir_y != -1:
                snake_dir_x = 0
                snake_dir_y = 1
            if event.key == pygame.K_w and snake_dir_y != 1:
                snake_dir_x = 0
                snake_dir_y = -1
            if event.key == pygame.K_a and snake_dir_x != 1:
                snake_dir_x = -1
                snake_dir_y = 0
            if event.key == pygame.K_d and snake_dir_x != -1:
                snake_dir_x = 1
                snake_dir_y = 0

    snake_body.insert(0, snake_head_coord)
    snake_body.pop(-1)

    # Updating snake head rect based on direction
    snake_head_x += (snake_dir_x * SNAKE_SIZE)
    snake_head_y += (snake_dir_y * SNAKE_SIZE)
    snake_head_coord = (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Checking for wall collision and body collision
    if snake_head_rect.left <= 0 or snake_head_rect.right >= WIN_WIDTH or snake_head_rect.top <= 0 or snake_head_rect.bottom >= WIN_HEIGHT or snake_head_coord in snake_body[1:]:
        print("Game Over")
        running = False

    # Checking snake head and food collision
    if snake_head_rect.colliderect(food_rect):
        score += 1
        score_txt = font.render("Score: " + str(score), True, SCORE_COLOR)
        food_x = random.randint(1, WIN_WIDTH - FOOD_SIZE)
        food_y = random.randint(1, WIN_HEIGHT - FOOD_SIZE)
        snake_body.append(snake_head_coord)


    # Updating game window
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(score_txt, score_rect)
    food_rect = pygame.draw.rect(WIN, FOOD_COLOR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))
    for body_coord in snake_body:
        pygame.draw.rect(WIN, SNAKE_COLOR, body_coord)
    snake_head_rect = pygame.draw.rect(WIN, SNAKE_COLOR, (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()