"""
pong.py
--------

Production-ready Pong game implemented using Pygame.
Includes structured logging, modular design, and clean class organization.
"""

import sys
import pygame
from libs.logger.game_logger import logger
from src.games.pong.game_objects.constants import GAME_TITLE, FPS, BACKGROUND_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT
from src.games.pong.game_objects.paddle import Paddle
from src.games.pong.game_objects.ball import Ball


# ---------------------------------------------------------------------------
# Game Class
# ---------------------------------------------------------------------------

class PongGame:
    """Main game class responsible for managing the Pong game loop."""

    def __init__(self) -> None:
        """Initialize the game window, clock, and objects."""
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

        # Initialize objects
        self.player_paddle = Paddle(self.display_surface)
        self.ball = Ball(self.display_surface)

        logger.info("PongGame initialized with window size %sx%s", WINDOW_WIDTH, WINDOW_HEIGHT)

    # -----------------------------------------------------------------------
    # Main Loop
    # -----------------------------------------------------------------------

    def run(self) -> None:
        """Start and maintain the main game loop."""
        logger.info("Starting main game loop")

        while self.is_running:
            self._handle_events()
            self._update()
            self._render()
            self.clock.tick(FPS)

        self._shutdown()

    # -----------------------------------------------------------------------
    # Event Handling
    # -----------------------------------------------------------------------

    def _handle_events(self) -> None:
        """Handle user and system events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Quit event detected. Stopping game loop.")
                self.is_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.player_paddle.move_right()

    # -----------------------------------------------------------------------
    # Game Logic
    # -----------------------------------------------------------------------

    def _update(self) -> None:
        """Update all game objects."""
        self.ball.move()
        self._handle_collisions()

    def _handle_collisions(self) -> None:
        """Handle collisions between the ball and paddle."""
        if self.ball.ball_rect.colliderect(self.player_paddle.rect):
            self.ball.bounce()
            # Optional: modify bounce angle based on paddle movement
            logger.debug("Collision detected between ball and paddle")

    # -----------------------------------------------------------------------
    # Rendering
    # -----------------------------------------------------------------------

    def _render(self) -> None:
        """Render all visual elements on the display surface."""
        self.display_surface.fill(BACKGROUND_COLOR)
        self.player_paddle.draw()
        self.ball.draw()
        pygame.display.flip()

    # -----------------------------------------------------------------------
    # Cleanup
    # -----------------------------------------------------------------------

    def _shutdown(self) -> None:
        """Safely close the game and release resources."""
        pygame.quit()
        logger.info("PongGame shutdown complete")
        sys.exit(0)


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    """Entry point for executing the Pong game."""
    try:
        game = PongGame()
        game.run()
    except KeyboardInterrupt:
        logger.info("Game terminated by user.")
        pygame.quit()
        sys.exit(0)
    except Exception as exc:
        logger.exception("Unhandled exception: %s", exc)
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()
