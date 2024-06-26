import pygame
from global_vars import WIDTH, HEIGHT

def initialize():
    print("Initializing Pygame...")
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.font.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    print("Pygame initialized successfully.")
    return screen, clock

# Call the init $fn when module is loaded
screen, clock = initialize()

print("init.py loaded and Pygame initialized successfully")

'''
init.py:

Initializes Pygame and returns the screen and clock.
Imports: pygame, WIDTH, HEIGHT from global_vars.py.
'''