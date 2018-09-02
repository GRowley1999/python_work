import pygame

class Rocket():
    
    def __init__(self, ai_settings, screen):
        """Initialize the rocket and its starting positon."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the rocket image and its rect.
        self.image = pygame.image.load('D:/Users/growl/Gregor Rowley/' + 
            'Programming/Python/python_work/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Flags to monitor the Rocket's movement.
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        # Start the rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Get a decimal value of the rocket's center x and y positions.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the rocket's movement based on movement flags."""
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.rocket_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery