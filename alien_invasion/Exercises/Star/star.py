import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('D:/Users/growl/Gregor Rowley/' + 
            'Programming/Python/python_work/alien_invasion/images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each star close to the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """Draw a star to the screen."""
        pygame.screen.blit(self.image, self.rect)