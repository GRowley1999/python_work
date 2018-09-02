class Settings():
    """A class to store all settings for Catch."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (255, 255, 255)

        # Catcher settings
        self.catcher_speed_factor = 1.5

        # Ball settings
        self.ball_speed_factor = 1
        self.ball_limit = 3