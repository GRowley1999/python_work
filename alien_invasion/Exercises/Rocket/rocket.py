import sys
import pygame
from rocket_class import Rocket
from rocket_settings import Settings
import game_functions as gf


pygame.init()

# Instantiate a Settings method.
ai_settings = Settings()

# Create a display window surface.
screen = pygame.display.set_mode((ai_settings.screen_width, 
    ai_settings.screen_height))
pygame.display.set_caption("Rocket")

# Make a Rocket class.
rocket = Rocket(ai_settings, screen)


while True:
    gf.check_events(rocket)
    rocket.update()
    gf.update_screen(ai_settings, screen, rocket)
