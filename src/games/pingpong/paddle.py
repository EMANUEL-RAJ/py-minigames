import pygame

from .constants import *


class Paddle:
    """
    Paddle class
    """
    def __init__(self, screen: pygame.Surface, y_position: int, score_position):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE, True)
        self.score = 0
        self.score_position = score_position
        self.update_score_text()
        self.rect = pygame.Rect(
            (GAME_SCREEN_WIDTH // 2 - PAD_WIDTH // 2, y_position)
            , (PAD_WIDTH, PAD_HEIGHT)
        )

    def update_score(self):
        self.score += 1
        self.update_score_text()

    def update_score_text(self):
        self.score_surface = self.font.render(str(self.score), True, GAME_OBJ_CLR)
        self.score_rect = self.score_surface.get_rect(topleft=self.score_position)

    def move_left(self):
        """
        Moves player paddle to left
        :return:
        """
        self.rect.centerx = self.rect.centerx - PAD_SPEED
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        """
        Moves player paddle to right
        :return:
        """
        self.rect.centerx = self.rect.centerx + PAD_SPEED
        if self.rect.right > GAME_SCREEN_WIDTH:
            self.rect.right = GAME_SCREEN_WIDTH

    def render(self):
        """
        Renders the paddle onto the screen
        :return:
        """
        pygame.draw.rect(self.screen, GAME_OBJ_CLR, self.rect)
        self.screen.blit(self.score_surface, self.score_rect)