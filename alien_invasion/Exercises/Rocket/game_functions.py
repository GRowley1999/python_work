import sys
import pygame

def check_keydown_events(event, rocket):
    """Respond to keypresses."""
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """Respond to keypresses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(ai_settings, screen, rocket):
    """Update images on the screen and flip to the new screen."""
     # Redraw the screen on each pass through the loop.
    screen.fill(ai_settings.bg_colour)
    
    # Draw a rocket to the screen.
    rocket.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()