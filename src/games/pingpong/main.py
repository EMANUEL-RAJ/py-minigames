import sys

import pygame

from .constants import *
from libs.logger.game_logger import logger
from .paddle import Paddle


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
        self.player = Paddle(self, self.screen, PLAYER_PAD_POSITION)
        self.bot = Paddle(self, self.screen, BOT_PAD_POSITION)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                logger.info("Game terminated by user.")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()

    def _update(self):
        pygame.display.update()

    def _render(self):
        self.screen.fill(GAME_BG_CLR)
        pygame.draw.line(self.screen, GAME_OBJ_CLR, SCREEN_DIV[0], SCREEN_DIV[1], 1)
        self.player.render()
        self.bot.render()
        self.clock.tick(GAME_FPS)

    def run(self):
        """
        Runs main game loop
        :return: None
        """
        while self.running:
            self._handle_events()
            self._update()
            self._render()

        pygame.quit()
        sys.exit(0)


def main() -> None:
    try:
        game = Game()
        game.run()
    except Exception as exc:
        logger.exception("Unhandled exception: %s", exc)


if __name__ == "__main__":
    main()
