import pygame

import sys

class Game_character():
    """A class which represents a game character."""

    def __init__(self, screen):
        """Initialize the game character and set it's starting position."""
        self.screen = screen

        # Load the game character and get its rect.
        self.image = pygame.image.load("D:/Users/growl/Gregor Rowley/" + 
            "Programming/Python/python_work/alien_invasion/images/pikachu.bmp") 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the game character's position on the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draws the game character to the screen."""
        self.screen.blit(self.image, self.rect)


screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Game Character")

character = Game_character(screen)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

    screen.fill((255, 255, 255))
    character.blitme()

    pygame.display.flip()