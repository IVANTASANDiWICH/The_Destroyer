import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from Shapiro"""

    def __init__(self, td_settings, screen, character):
        """Create a bullet object at Shapiro's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pg.Rect(0, 0, td_settings.bullet_width,
                            td_settings.bullet_height)
        self.rect.centery = character.centery
        self.rect.right = character.rect.right

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

        self.color = td_settings.bullet_color
        self.speed_factor = td_settings.bullet_speed_factor

    def update(self):
        """Move the bullet across the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect positions.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pg.draw.rect(self.screen, self.color, self.rect)

