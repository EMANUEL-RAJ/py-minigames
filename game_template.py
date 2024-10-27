# --- Importing Packages ---
import sys
import pygame

# --- Setting Constants and Variables ---
# colors
WHITE = (255, 255, 255)

# game constants
WIN_WIDTH = 500
WIN_HEIGHT = 500
FPS = 60

running = True

# --- Initializing Pygame and Setting Clock---
pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill(WHITE)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()