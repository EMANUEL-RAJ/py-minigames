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

    def __init__(self, player_bullet_group):
        """
        Initializing the player
        """
        super().__init__()
        self.player_bullet_group = player_bullet_group
        self.image = pygame.image.load(SHIP_PATH)
        self.rect = self.image.get_rect(centerx=WIN_WIDTH //2, bottom=WIN_HEIGHT - 5)
        self.lives = 5
        self.velocity = 8
        self.shoot_sound = pygame.mixer.Sound(SHIP_FIRE_SOUND_PATH)


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


# --- creating bullet sprite groups ---
player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

# --- creating player object and sprite group
player_group = pygame.sprite.Group()
player = Player(player_bullet_group)  # passing player bullet group
player_group.add(player)

# --- creating alien group and alien objects will be added inside Game class
alien_group = pygame.sprite.Group()

# --- creating Game object ---
game = Game()

# --- main game loop ---
running = True
while running:
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # filling window
    window.fill(BLACK)
    # update and display all sprite groups
    player_group.update()
    player_group.draw(window)

    alien_group.update()
    alien_group.draw(window)

    player_bullet_group.update()
    player_bullet_group.draw(window)

    alien_bullet_group.update()
    alien_bullet_group.draw(window)

    # update and draw game object
    game.update()
    game.draw()

    pygame.display.update()
    clock.tick(FPS)
