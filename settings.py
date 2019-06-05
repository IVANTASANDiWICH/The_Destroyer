class Settings():
    """A class to store all the settings for 'The Destroyer'."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (25, 25, 25)

        # Character settings
        self.character_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 70
        self.bullet_height = 85
        self.bullet_color = 250, 0, 0
        self.bullets_allowed = 4


