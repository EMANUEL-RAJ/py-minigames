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
        self.rect = self.image.get_rect(centerx=WIN_WIDTH // 2, bottom=WIN_HEIGHT - 5)
        self.lives = 5
        self.velocity = 8
        self.shoot_sound = pygame.mixer.Sound(SHIP_FIRE_SOUND_PATH)

    def update(self):
        """
        Updates the player
        """
        keys = pygame.key.get_pressed()
        # moving player within bounds of window
        if keys[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocity

    def fire(self):
        """
        Fires a laser beam
        """
        # restricting the number of bullets on screen at a time
        if len(self.player_bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.player_bullet_group)

    def reset(self):
        """
        Resets the player position
        """
        self.rect.centerx = WIN_WIDTH // 2


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

    def __init__(self, player_x_pos, player_y_pos, bullet_group):
        """
        Initializing the player bullet
        """
        super().__init__()
        self.image = pygame.image.load(GREEN_BULLET_PATH)
        self.rect = self.image.get_rect()
        self.rect.centerx = player_x_pos
        self.rect.centery = player_y_pos
        self.velocity = 10

        bullet_group.add(self)  # adding bullet to bullet group

    def update(self):
        """
        Updates the bullet
        """
        self.rect.centery -= self.velocity
        # removing bullet if it goes off the screen
        if self.rect.bottom < 0:
            self.kill()


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
        # player fires
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

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
