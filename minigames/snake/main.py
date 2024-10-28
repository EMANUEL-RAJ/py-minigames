# --- Importing Packages ---
import sys
import pygame

from config import *

# --- Game Variables ---
running = True
score = 0

# --- Initializing Pygame and Setting Clock---
pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

# --- Building In-Game Assets ---
font = pygame.font.SysFont("freesansbold", 15)
score_txt = font.render("Score: " + str(score), True, SCORE_COLOR)
score_rect = score_txt.get_rect(topleft=SCORE_RECT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(score_txt, score_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()