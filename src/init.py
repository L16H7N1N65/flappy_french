import pygame
from global_vars import WIDTH, HEIGHT, BACKGROUND_IMAGE_PATH, FLOOR_IMAGE_PATH

def initialize():
    # Load and scale the background image
    background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Load and scale the floor image
    floor_image = pygame.image.load(FLOOR_IMAGE_PATH).convert_alpha()
    floor_height = floor_image.get_height() // 10  # Adjust floor height
    floor_image = pygame.transform.scale(floor_image, (WIDTH, floor_height))

    return background_image, floor_image

