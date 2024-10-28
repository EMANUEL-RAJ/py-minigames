# --- Importing Packages ---
import sys
import pygame
import random

from config import *

# --- Game Variables ---
running = True
new_game = True
game_over = False
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
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load(ICON_PATH))
clock = pygame.time.Clock()

# --- Building In-Game Assets ---
# game font
font = pygame.font.SysFont("freesansbold", 15)
score_txt = font.render("Score: " + str(score), True, SCORE_COLOR)
score_rect = score_txt.get_rect(topleft=SCORE_RECT)
new_game_txt = font.render(" Press any key to start ", True, SCORE_COLOR)
new_game_rect = new_game_txt.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
game_over_txt = font.render(" Game Over. Score: " + str(score) + " . Press any key to start new game", True, SCORE_COLOR)
game_over_rect = game_over_txt.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
# snake
snake_head_coord = (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE)
snake_head_rect = pygame.draw.rect(WIN, SNAKE_COLOR, snake_head_coord)
# food
food_rect = pygame.draw.rect(WIN, FOOD_COLOR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

# --- Main Game Loop ---
while running:
    while new_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                new_game = False
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(new_game_txt, new_game_rect)
        pygame.display.update()
    while game_over:
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(game_over_txt, game_over_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                score = 0
                snake_head_x = WIN_WIDTH // 2
                snake_head_y = WIN_HEIGHT // 2
                snake_dir_x = 1
                snake_dir_y = 0
                snake_body = []
                food_x = random.randint(1, WIN_WIDTH - FOOD_SIZE)
                food_y = random.randint(1, WIN_HEIGHT - FOOD_SIZE)
                game_over = False
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key in (pygame.K_s, pygame.K_DOWN)) and snake_dir_y != -1:
                snake_dir_x = 0
                snake_dir_y = 1
            if (event.key in (pygame.K_w, pygame.K_UP)) and snake_dir_y != 1:
                snake_dir_x = 0
                snake_dir_y = -1
            if (event.key in (pygame.K_a, pygame.K_LEFT)) and snake_dir_x != 1:
                snake_dir_x = -1
                snake_dir_y = 0
            if (event.key in (pygame.K_d, pygame.K_RIGHT)) and snake_dir_x != -1:
                snake_dir_x = 1
                snake_dir_y = 0

    # Adding head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list
    snake_body.insert(0, snake_head_coord)
    snake_body.pop(-1)

    # Updating snake head rect based on direction
    snake_head_x += (snake_dir_x * SNAKE_SIZE)
    snake_head_y += (snake_dir_y * SNAKE_SIZE)
    snake_head_coord = (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Checking for wall collision and body collision
    if (
            snake_head_rect.left <= 0
            or snake_head_rect.right >= WIN_WIDTH
            or snake_head_rect.top <= 0
            or snake_head_rect.bottom >= WIN_HEIGHT
            or snake_head_coord in snake_body[1:]
    ):
        game_over = True
        game_over_txt = font.render(" Game Over. Score: " + str(score) + " . Press any key to start new game", True, SCORE_COLOR)

    # Checking snake head and food collision
    if snake_head_rect.colliderect(food_rect):
        score += 1
        score_txt = font.render("Score: " + str(score), True, SCORE_COLOR)
        food_x = random.randint(1, WIN_WIDTH - FOOD_SIZE)
        food_y = random.randint(1, WIN_HEIGHT - FOOD_SIZE)
        snake_body.append(snake_head_coord)

    # Updating game window
    WIN.fill(BACKGROUND_COLOR)
    food_rect = pygame.draw.rect(WIN, FOOD_COLOR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))
    for body_coord in snake_body:
        pygame.draw.rect(WIN, SNAKE_COLOR, body_coord)
    snake_head_rect = pygame.draw.rect(WIN, SNAKE_COLOR, snake_head_coord)
    WIN.blit(score_txt, score_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
