# --- Importing Packages ---
import sys
import pygame

from config import *

running = True

# --- Initializing Pygame and Setting Clock---
pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()


# --- Game Classes ---
class Paddle:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 5
        self.height = 75
        self.speed = 10
        self.paddle = pygame.draw.rect(WIN, PADDLE_COLOR, (self.x_pos, self.y_pos, self.width, self.height))

    def draw(self):
        self.paddle = pygame.draw.rect(WIN, PADDLE_COLOR, (self.x_pos, self.y_pos, self.width, self.height))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y_pos >= 0:
            self.y_pos -= self.speed
        if keys[pygame.K_s] and (self.y_pos + self.height) <= WIN_HEIGHT:
            self.y_pos += self.speed


player = Paddle(570, 250)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill(BACKGROUND_COLOR)
    player.update()
    player.draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
