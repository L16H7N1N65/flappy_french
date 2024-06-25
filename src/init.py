# init.py

import pygame
from global_vars import WIDTH, HEIGHT

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock
