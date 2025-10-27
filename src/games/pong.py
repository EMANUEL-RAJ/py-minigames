"""
pong.py
--------

A basic Pong game implemented using Pygame.

"""

import sys
import pygame
from libs.logger.game_logger import logger

# ---------------------------------------------------------------------------
# Configuration Constants
# ---------------------------------------------------------------------------

GAME_TITLE: str = "Pong"
WINDOW_WIDTH: int = 500
WINDOW_HEIGHT: int = 500

BACKGROUND_COLOR: tuple[int, int, int] = (0, 0, 0)
PADDLE_COLOR: tuple[int, int, int] = (255, 255, 255)

FPS: int = 60
PADDLE_WIDTH: int = 60
PADDLE_HEIGHT: int = 8
PADDLE_SPEED: int = 8


# ---------------------------------------------------------------------------
# Paddle Class
# ---------------------------------------------------------------------------

class Paddle:
    """Represents the player paddle and handles its movement and rendering."""

    def __init__(self, display_surface: pygame.Surface) -> None:
        """Initialize the paddle object."""
        self.display_surface = display_surface
        self.rect = pygame.Rect(
            (WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2, WINDOW_HEIGHT - 40),
            (PADDLE_WIDTH, PADDLE_HEIGHT),
        )
        self.speed = PADDLE_SPEED

    def move_left(self) -> None:
        """Move the paddle left while ensuring it stays within the screen."""
        self.rect.x = max(self.rect.x - self.speed, 0)
        logger.debug("Paddle moved left to x=%d", self.rect.x)

    def move_right(self) -> None:
        """Move the paddle right while ensuring it stays within the screen."""
        max_x = WINDOW_WIDTH - self.rect.width
        self.rect.x = min(self.rect.x + self.speed, max_x)
        logger.debug("Paddle moved right to x=%d", self.rect.x)

    def draw(self) -> None:
        """Render the paddle on the display surface."""
        pygame.draw.rect(self.display_surface, PADDLE_COLOR, self.rect)


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

        # Initialize game objects
        self.player_paddle = Paddle(self.display_surface)

        logger.info("PongGame initialized with window size %s×%s", WINDOW_WIDTH, WINDOW_HEIGHT)

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

        # Continuous key input for smooth paddle control
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
        # Future expansion: ball movement, collision, score tracking
        pass

    # -----------------------------------------------------------------------
    # Rendering
    # -----------------------------------------------------------------------

    def _render(self) -> None:
        """Render all visual elements on the display surface."""
        self.display_surface.fill(BACKGROUND_COLOR)
        self.player_paddle.draw()
        pygame.display.flip()

    # -----------------------------------------------------------------------
    # Cleanup
    # -----------------------------------------------------------------------

    def _shutdown(self) -> None:
        """Safely close the game and release resources."""
        pygame.quit()
        logger.info("PongGame shutdown complete")
        sys.exit()


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    """Entry point for executing the Pong game."""
    try:
        game = PongGame()
        game.run()
    except Exception as exc:
        logger.exception("Unhandled exception: %s", exc)
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()
