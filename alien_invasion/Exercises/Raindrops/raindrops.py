import pygame
from pygame.sprite import Group
from settings import Settings
from raindrop import Raindrop
import raindrops_functions as rf

def run_raindrops():
    """Initialise the game and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrops")

    # Make a group of raindrops
    raindrops = Group()

    # Create a grid of raindrops
    rf.create_fleet(screen, ai_settings, raindrops)

    # Start the main loop for the program
    while True:
        rf.check_events()
        rf.update_raindrop(ai_settings, screen, raindrops)
        rf.update_screen(ai_settings, screen, raindrops)

run_raindrops()