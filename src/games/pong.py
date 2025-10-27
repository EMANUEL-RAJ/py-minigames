import pygame

from src.logger.game_logger import logger

# Constants:
GAME_NAME = "Pong"
DISPLAY_DIM = (500, 500)
BLACK = (0, 0, 0)
FPS = 60

pygame.init()
pygame.display.set_caption(GAME_NAME)


class Game:
    def __init__(self):
        self.DISPLAY = pygame.display.set_mode(DISPLAY_DIM)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                logger.info(event)
                if event.type == pygame.QUIT:
                    self.running = False
            self.DISPLAY.fill(BLACK)
            self.clock.tick(FPS)
            pygame.display.update()

        pygame.quit()


game = Game()
game.run()
