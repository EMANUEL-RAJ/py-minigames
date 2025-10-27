"""
pong.py
--------

A basic Pong game loop using Pygame.
Includes structured logging with Rich.
"""
import sys

import pygame
from src.logger.game_logger import logger


# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------
GAME_TITLE = "Pong"
WINDOW_SIZE = (500, 500)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60


# ---------------------------------------------------------------------------
# Game Class
# ---------------------------------------------------------------------------
class PongGame:
    """Main game class responsible for initializing and running Pong."""

    def __init__(self) -> None:
        """Initialize Pygame display, clock, and game state."""
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)

        self.display_surface = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.is_running = True

        logger.info("PongGame initialized with window size %s", WINDOW_SIZE)

    # -----------------------------------------------------------------------
    # Main Loop
    # -----------------------------------------------------------------------
    def run(self) -> None:
        """Run the main game loop."""
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
        """Handle user input and system events."""
        for event in pygame.event.get():
            logger.debug("Event detected: %s", event)
            if event.type == pygame.QUIT:
                self.is_running = False

    # -----------------------------------------------------------------------
    # Game Logic
    # -----------------------------------------------------------------------
    def _update(self) -> None:
        """Update game state (placeholder for gameplay logic)."""
        pass  # Future: add ball & paddle updates

    # -----------------------------------------------------------------------
    # Rendering
    # -----------------------------------------------------------------------
    def _render(self) -> None:
        """Draw all visual elements on the screen."""
        self.display_surface.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    # -----------------------------------------------------------------------
    # Cleanup
    # -----------------------------------------------------------------------
    def _shutdown(self) -> None:
        """Cleanly exit the game and shut down Pygame."""
        pygame.quit()
        logger.info("Game shutdown complete")
        sys.exit()


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
def main() -> None:
    """Entry point for running the Pong game."""
    try:
        game = PongGame()
        game.run()
    except Exception as exc:
        logger.exception("Unhandled exception occurred: %s", exc)
        pygame.quit()


if __name__ == "__main__":
    main()
