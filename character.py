import pygame as pg

class Character():

    def __init__(self, td_settings, screen):
        """Initialize the character and set its starting position."""
        self.screen = screen
        self.td_settings = td_settings

        # Load the character image and get its rect.
        self.image = pg.image.load('images/ben_shapiro.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the character's center.
        self.centery = float(self.rect.centery)
        self.centerx = float(self.rect.centerx)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the character's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.td_settings.character_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.td_settings.character_speed_factor
        if self.moving_right and self.rect.right < 500:
            self.centerx += self.td_settings.character_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.td_settings.character_speed_factor

        # Update rect object from self.center.
        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)