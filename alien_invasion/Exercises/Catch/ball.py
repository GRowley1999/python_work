import pygame
from random import randint
from pygame.sprite import Sprite

class Ball(Sprite):
    """A class to represent a ball."""

    def __init__(self, ai_settings, screen):
        """Initialise the ball and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('D:/Users/growl/Gregor Rowley/' + 
            'Programming/Python/python_work/alien_invasion/images/ball.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = randint(self.rect.width + 0, 1200 - self.rect.width)
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.y = float(self.rect.y)
        
    def blitme(self):
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)
    

    def update(self):
        """Move the alien right."""
        self.y += self.ai_settings.ball_speed_factor
        self.rect.y = self.y

    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True