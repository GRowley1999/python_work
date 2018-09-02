import pygame
import sys
from raindrop import Raindrop
from settings import Settings

def check_events():
    """Monitor for mouse and keyboard events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
def update_screen(settings, screen, raindrops):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen on each pass through the loop.
    screen.fill(settings.bg_color)

    # Draw all raindrops to the screen.
    raindrops.draw(screen)

    # Flip to the most recently drawn screen.
    pygame.display.flip()

def get_number_raindrops_x(settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = (settings.screen_width - (2 * raindrop_width))
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x


def get_number_rows(settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = (settings.screen_height - (3 * raindrop_height))
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows


def create_raindrop(screen, settings, raindrops, raindrop_number, row_number):
    """Create an raindrop and place it in the row."""
    raindrop = Raindrop(screen, settings)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = (raindrop.rect.height + (2 * raindrop.rect.height 
        * row_number))
    raindrops.add(raindrop)

    
def create_fleet(screen, settings, raindrops):
    """Create a full fleet of raindrops."""
    # Create an raindrop and find the number of raindrops in a row.
    # Spacing between each raindrop is equal to one raindrop width.
    raindrop = Raindrop(screen, settings)
    number_raindrops_x = get_number_raindrops_x(settings, raindrop.rect.width)
    number_rows = get_number_rows(settings, raindrop.rect.height)

    # Create the first row of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
        # Create an raindrop and place it in the row.
            create_raindrop(screen, settings, raindrops, raindrop_number,
                row_number)

def check_raindrop_edges(settings, screen, raindrops):
    """Produce a new row of raindrops if a row drops below the screen."""
    for raindrop in raindrops.sprites():
        if raindrop.check_edges():
            
            # Empty the list of raindrops.
            raindrops.empty()

            # Create new grid of raindrops.
            create_fleet(settings, screen, raindrops)



def update_raindrop(settings, screen, raindrops):
    """
    Check if a row of raindrops has dropped below the screen and respond 
    accordingly, and move the raindrops continually down the screen.
    """
    check_raindrop_edges(settings, screen, raindrops)
    raindrops.update()