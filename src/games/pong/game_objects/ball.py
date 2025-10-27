"""
Module contains ball class
"""
import math
import time
import random
import pygame
from libs.logger.game_logger import logger
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, BALL_RADIUS, BALL_COLOR, BALL_INIT_X_VELOCITY, \
    BALL_INIT_Y_VELOCITY, BALL_RESET_DELAY, BALL_SPEED


# ---------------------------------------------------------------------------
# Ball Class
# ---------------------------------------------------------------------------

class Ball:
    """Represents the Pong ball with movement and wall collision logic."""

    def __init__(self, display_surface: pygame.Surface) -> None:
        """Initialize the ball at the center of the screen."""
        pygame.init()
        self.display_surface = display_surface
        self.ball_rect = None
        self.reset()

    def _calculate_velocity(self):
        direction = random.choice([1, -1])
        if direction == 1:
            angle_deg = random.uniform(30, 150)
        else:
            angle_deg = random.uniform(210, 330)

        angle_rad = math.radians(angle_deg)
        self.x_velocity = math.cos(angle_rad) * BALL_SPEED
        self.y_velocity = math.sin(angle_rad) * BALL_SPEED

    def reset(self) -> None:
        """Reset the ball to the center with a random initial direction."""
        self.ball_rect = pygame.Rect(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2,
            BALL_RADIUS * 2,
            BALL_RADIUS * 2,
        )
        self._calculate_velocity()
        logger.info("Ball reset to center with velocity (%d, %d)", self.x_velocity, self.y_velocity)
        time.sleep(BALL_RESET_DELAY)

    def move(self) -> None:
        """Move the ball and handle wall collisions."""
        self.ball_rect.x += self.x_velocity
        self.ball_rect.y += self.y_velocity

        # Wall collisions
        if self.ball_rect.left <= 0 or self.ball_rect.right >= WINDOW_WIDTH:
            self.x_velocity *= -1
            logger.debug("Ball bounced horizontally: new x_velocity=%d", self.x_velocity)

        if self.ball_rect.top <= 0:
            logger.info("Player scored a point.")
            self.reset()

        elif self.ball_rect.bottom >= WINDOW_HEIGHT:
            logger.info("Bot scored a point.")
            self.reset()

    def bounce(self) -> None:
        """Reverse the Y-direction to simulate a bounce."""
        self.y_velocity *= -1
        logger.debug("Ball bounced off paddle: new y_velocity=%d", self.y_velocity)

    def draw(self) -> None:
        """Render the ball as a circle."""
        pygame.draw.circle(self.display_surface, BALL_COLOR, self.ball_rect.center, BALL_RADIUS)
