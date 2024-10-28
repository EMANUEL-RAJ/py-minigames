# --- Importing Packages ---
import sys
import pygame

from config import *

# --- Game Variables ---
running = True

# --- Initializing Pygame and Setting Clock---
pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill(BACKGROUND_COLOR)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()