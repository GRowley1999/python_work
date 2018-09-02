import pygame
from pygame.sprite import Group
from ai_settings import Settings
from star import Star
import game_funtions as gf

def run_stars():
    """Initialise the game and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Stars")

    # Make a group of stars
    stars = Group()

    # Create a grid of stars
    gf.create_grid(ai_settings, screen, stars)

    # Start the main loop for the program
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, stars)

run_stars()