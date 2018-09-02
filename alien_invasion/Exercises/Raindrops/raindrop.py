import pygame
from pygame.sprite import Sprite
from settings import Settings

class Raindrop(Sprite):
    """A class to represent a single star."""

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('D:/Users/growl/Gregor Rowley/' + 
            'Programming/Python/python_work/alien_invasion/images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each star close to the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def blitme(self):
        """Draw a star to the screen."""
        pygame.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Return true if a raindrop drops past the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        

    def update(self):
        """Move the raindrops down the screen."""
        self.y += self.settings.raindrop_speed_factor
        self.rect.y = self.y