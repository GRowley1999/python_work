import pygame

import sys

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Blue Sky")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 255))
    
    pygame.display.flip()