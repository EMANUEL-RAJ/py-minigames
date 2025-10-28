import pygame

from .constants import *


class Paddle:
    def __init__(self, game, screen: pygame.Surface, y_position: int):
        self.game = game
        self.screen = screen
        self.score = 0
        self.rect = pygame.Rect(
            (GAME_SCREEN_WIDTH // 2 - PAD_WIDTH // 2, y_position)
            , (PAD_WIDTH, PAD_HEIGHT)
        )

    def move_left(self):
        self.rect.centerx = self.rect.centerx - PAD_SPEED
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.centerx = self.rect.centerx + PAD_SPEED
        if self.rect.right > GAME_SCREEN_WIDTH:
            self.rect.right = GAME_SCREEN_WIDTH

    def render(self):
        pygame.draw.rect(self.screen, GAME_OBJ_CLR, self.rect)