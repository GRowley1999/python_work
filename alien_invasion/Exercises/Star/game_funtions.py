import pygame
import sys
from star import Star
from random import randint

def check_events():
    """Monitor for mouse and keyboard events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
def update_screen(ai_settings, screen, stars):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen on each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Draw all stars to the screen.
    stars.draw(screen)

    # Flip to the most recently drawn screen.
    pygame.display.flip()

def create_star(screen, stars, star_number, row_number):
    """Create a star and place it in the row."""
    star = Star(screen)
    star.x = randint(0, 1200)
    star.rect.x = star.x
    star.rect.y = randint(0, 800)
    stars.add(star)

def get_number_stars_x(ai_settings, star_width):
    """Determine the number of stars that fit into a row."""
    available_space_x = ai_settings.screen_width - (2 * star_width)
    number_aliens_x = int(available_space_x / (2 * star_width))
    return number_aliens_x

def get_number_rows(ai_settings, star_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = ai_settings.screen_height - (2 * star_height)
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows


def create_grid(ai_settings, screen, stars):
    """Create a grid of stars"""
    # Create a star and find the number of stars in a row.
    # Spacing between each star is equal to one star width.
    star = Star(screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    # Create the grid of aliens
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(screen, stars, star_number, row_number)
