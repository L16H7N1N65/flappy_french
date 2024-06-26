# draw_start_screen.py


import pygame
from global_vars import screen, WIDTH, HEIGHT


# Initialize pygame to avoid errors when loading images
pygame.init()

print("Loading images...")
# Pre-load and scale images to improve performance
bg_initial = pygame.image.load("../assets/bg_initial.png")
bg_initial_scaled = pygame.transform.scale(bg_initial, (WIDTH, HEIGHT))
screen.blit(bg_initial_scaled, (0, 0))
print("Background image loaded and scaled.")

logo = pygame.image.load("../assets/logo.png")
logo_scaled = pygame.transform.scale(logo, (logo.get_width() // 1.6, logo.get_height() // 1.6))
print("Logo image loaded and scaled.")

initial_start = pygame.image.load("../assets/initial_start.png")
initial_start_scaled = pygame.transform.scale(initial_start, (initial_start.get_width() // 1.6, initial_start.get_height() // 1.6))
print("Initial start image loaded and scaled.")

def draw_start_screen(screen, blink):
    print("Drawing start screen...")
    screen.blit(bg_initial_scaled, (0, 0))
    logo_rect = logo_scaled.get_rect(topright=(WIDTH - 25, 18))
    screen.blit(logo_scaled, logo_rect)
    print("Logo placed.")

    initial_start_rect = initial_start.get_rect(bottomright=(WIDTH - 25, HEIGHT - 25))
    if blink:
        screen.blit(initial_start, initial_start_rect)
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