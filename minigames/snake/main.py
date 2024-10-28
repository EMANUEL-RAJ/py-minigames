# --- Importing Packages ---
import sys
import pygame

from config import *

# --- Game Variables ---
running = True
score = 0
snake_head_x = WIN_WIDTH // 2
snake_head_y = WIN_HEIGHT // 2
snake_dir_x = 1
snake_dir_y = 0

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
snake_head_rect = pygame.draw.rect(WIN, SNAKE_COLOR, (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE))

# --- Main Game Loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                snake_dir_x = 0
                snake_dir_y = 1
            if event.key == pygame.K_w:
                snake_dir_x = 0
                snake_dir_y = -1
            if event.key == pygame.K_a:
                snake_dir_x = -1
                snake_dir_y = 0
            if event.key == pygame.K_d:
                snake_dir_x = 1
                snake_dir_y = 0

    # Updating snake head rect based on direction
    snake_head_x += (snake_dir_x * SNAKE_SIZE)
    snake_head_y += (snake_dir_y * SNAKE_SIZE)

    # Updating game window
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(score_txt, score_rect)
    snake_head_rect = pygame.draw.rect(WIN, SNAKE_COLOR, (snake_head_x, snake_head_y, SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()