import pygame
from src.global_vars import config

def initialize():
    print("Initializing Pygame...")
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))  # Correct the parameter passing here
    pygame.font.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    print("Pygame initialized successfully.")
    return screen, clock

# Initialize Pygame when the module is loaded
screen, clock = initialize()

print("init.py loaded and Pygame initialized successfully")


'''
init.py:

Initializes Pygame and returns the screen and clock.
Imports: pygame, WIDTH, HEIGHT from global_vars.py.
'''