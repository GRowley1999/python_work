import pygame
from catcher import Catcher
from ball import Ball
from settings import Settings
import game_functions as gf 
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    """Initialise the game and create a screen object.""" 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")

    # Create an instance to store game stats.
    stats = GameStats(ai_settings)

    # Make a catcher and a ball and groups of both
    catcher = Catcher(ai_settings, screen)
    ball = Ball(ai_settings, screen)
    balls = Group()
    balls.add(ball)
    

    # Main game loop
    while True:
        gf.check_events(ai_settings, screen, catcher)

        if stats.game_active:
            catcher.update()
            gf.update_balls(ai_settings, stats, screen, catcher, balls)
        
        gf.update_screen(ai_settings, screen, catcher, balls)


run_game()