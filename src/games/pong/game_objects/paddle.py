"""
Module contains paddle class
"""
import pygame

from libs.logger.game_logger import logger
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, PADDLE_COLOR


# ---------------------------------------------------------------------------
# Paddle Class
# ---------------------------------------------------------------------------

class Paddle:
    """Represents the player paddle and handles its movement and rendering."""

    def __init__(self, display_surface: pygame.Surface) -> None:
        """Initialize the paddle object."""
        pygame.init()
        self.display_surface = display_surface
        self.rect = pygame.Rect(
            (WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2, WINDOW_HEIGHT - 40),
            (PADDLE_WIDTH, PADDLE_HEIGHT),
        )
        self.speed: int = PADDLE_SPEED

    def move_left(self) -> None:
        """Move the paddle left within window boundaries."""
        old_x = self.rect.x
        self.rect.x = max(self.rect.x - self.speed, 0)
        logger.debug("Paddle moved left: %d -> %d", old_x, self.rect.x)

    def move_right(self) -> None:
        """Move the paddle right within window boundaries."""
        old_x = self.rect.x
        max_x = WINDOW_WIDTH - self.rect.width
        self.rect.x = min(self.rect.x + self.speed, max_x)
        logger.debug("Paddle moved right: %d -> %d", old_x, self.rect.x)

    def draw(self) -> None:
        """Render the paddle on the display surface."""
        pygame.draw.rect(self.display_surface, PADDLE_COLOR, self.rect)
