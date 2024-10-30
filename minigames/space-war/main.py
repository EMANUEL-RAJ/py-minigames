# --- importing packages and constants---
import pygame, sys, random
from config import *

# --- initializing pygame ---
pygame.init()

# --- set display ---
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(TITLE)

# --- set clock ---
clock = pygame.time.Clock()


# --- game classes ---
class Game():
    def __init__(self):
        """
        Initializing the game
        """
        pass

    def update(self):
        """
        Updates the game
        """
        pass

    def draw(self):
        """
        Draws the HUD and other information on the window
        """
        pass

    def shift_aliens(self):
        """
        Shift the alien wave down the window and reverses direction
        """
        pass

    def check_collision(self):
        """
        Check for collisions
        """
        pass

    def check_round_completion(self):
        """
        Check to see if a player has completed the round
        """
        pass

    def check_game_status(self):
        """
        Checks status of game and how the ship died
        """
        pass

    def start_new_round(self):
        """
        Starts a new round
        """
        pass

    def pause_game(self):
        """
        Pauses the game
        """
        pass

    def reset_game(self):
        """
        Resets the game
        """
        pass


class Player(pygame.sprite.Sprite):
    """
    Class to model and control the player ship
    """

    def __init__(self):
        """
        Initializing the player
        """
        super().__init__()
        pass

    def update(self):
        """
        Updates the player
        """
        pass

    def fire(self):
        """
        Fires a laser beam
        """
        pass

    def reset(self):
        """
        Resets the player position
        """
        pass


class Alien(pygame.sprite.Sprite):
    """
    Class to model and control the enemy alien
    """

    def __init__(self):
        """
        Initializing the alien
        """
        super().__init__()
        pass

    def update(self):
        """
        Updates the alien
        """
        pass

    def fire(self):
        """
        Fires a laser beam
        """
        pass

    def reset(self):
        """
        Resets the alien position
        """
        pass


class PlayerBullet(pygame.sprite.Sprite):
    """
    Class to model a bullet fired by the player ship
    """

    def __init__(self):
        """
        Initializing the player bullet
        """
        super().__init__()
        pass

    def update(self):
        """
        Updates the bullet
        """
        pass


class AlienBullet(pygame.sprite.Sprite):
    """
    Class to model a bullet fired by the enemy alien
    """

    def __init__(self):
        """
        Initializing the alien bullet
        """
        super().__init__()
        pass

    def update(self):
        """
        Updates the bullet
        """
        pass


# --- main game loop ---
running = True
while running:
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)
