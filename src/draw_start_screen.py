#draw_start_screen.py

import pygame
from global_vars import config

# Initialize pygame to avoid errors when loading images
pygame.init()

print("Loading images...")
# Pre-load and scale images to improve performance
bg_initial = pygame.image.load(config.BACKGROUND_INITIAL_PATH).convert()
bg_initial_scaled = pygame.transform.scale(bg_initial, (config.WIDTH, config.HEIGHT))
print("Background image loaded and scaled.")

logo = pygame.image.load(config.LOGO_IMAGE_PATH).convert_alpha()
logo_scaled = pygame.transform.scale(logo, (logo.get_width() // 1.6, logo.get_height() // 1.6))
print("Logo image loaded and scaled.")

initial_start = pygame.image.load(config.INITIAL_START_IMAGE_PATH).convert_alpha()
initial_start_scaled = pygame.transform.scale(initial_start, (initial_start.get_width() // 1.1, initial_start.get_height() // 1.1))
print("Initial start image loaded and scaled.")

def draw_start_screen(screen, blink):
    print("Drawing start screen...")
    screen.blit(bg_initial_scaled, (0, 0))
    logo_rect = logo_scaled.get_rect(topright=(config.WIDTH - 25, 18))
    screen.blit(logo_scaled, logo_rect)
    print("Logo placed.")

    initial_start_rect = initial_start_scaled.get_rect(bottomright=(config.WIDTH - 25, config.HEIGHT - 25))
    if blink:
        screen.blit(initial_start_scaled, initial_start_rect)
        print("Initial start image placed with blinking effect.")
    else:
        print("Blinking effect not applied.")
    print("Start screen drawn.")



'''
draw_start_screen.py:

Draws the initial screen.
Needs: pygame, WIDTH, HEIGHT
bg_initial, logo, initial_start images from assets but loaded direclty here.
'''