import sys

import pygame

from catcher import Catcher

from ball import Ball

from random import randint

from time import sleep


def check_keydown_events(event, ai_settings, screen, catcher):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, catcher):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = False


def check_events(ai_settings, screen, catcher):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, catcher)
            elif event.type == pygame.KEYUP:        
                check_keyup_events(event, catcher)

def update_screen(ai_settings, screen, catcher, balls):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_colour)

    # Draw a catcher and ball to the screen.
    catcher.blitme()
    balls.draw(screen)


    # Make the most recently drawn screen visible.
    pygame.display.flip()


def check_balls_edge(ai_settings, stats, screen, catcher, balls):
    """Respond appropriately if any have reached the bottom of the screen."""
    if stats.balls_left > 0:
        for ball in balls.sprites():
            if ball.check_edges():

                # Decrement ships_left.
                stats.balls_left -= 1

                # Empty the list of all balls
                balls.empty()

                # Create a new ball and center the ship.
                create_new_ball(ai_settings, screen, balls)
                catcher.center_catcher()

                # Pause.
                sleep(0.5)
    else:
        stats.game_active = False

def update_balls(ai_settings, stats, screen, catcher, balls):
    """Move the position of balls."""
    balls.update()
    check_balls_edge(ai_settings, stats, screen, catcher, balls)

    if pygame.sprite.spritecollideany(catcher, balls):
        balls.empty()
        create_new_ball(ai_settings, screen, balls)

def create_new_ball(ai_settings, screen, balls):
    """Create a new ball."""
    ball = Ball(ai_settings, screen)
    ball.rect.y = ball.rect.height
    ball.rect.x = randint(ball.rect.width + 0, 800 - ball.rect.width)
    balls.add(ball)
