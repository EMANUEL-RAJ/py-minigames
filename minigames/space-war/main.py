# --- importing packages and constants---
import pygame, sys, random
from config import *

# --- initializing pygame ---
pygame.init()

# --- set display ---
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(TITLE)

# --- set clock ---
clock = pygame.time.Clock()

# --- main game loop ---
running = True
while running:
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)