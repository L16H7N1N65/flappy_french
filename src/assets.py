#assets.py

import pygame
import sys
from src.global_vars import config

def load_images(image_paths, size):
    images = []
    for path in image_paths:
        try:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, size)
            images.append(image)
        except pygame.error as e:
            print(f"Failed to load image at {path}: {e}")
            sys.exit(1)
    return images

def load_sounds(sound_paths):
    sounds = []
    for path in sound_paths:
        try:
            sound = pygame.mixer.Sound(path)
            sounds.append(sound)
        except pygame.error as e:
            print(f"Failed to load sound at {path}: {e}")
            sys.exit(1)
    return sounds

def load_digit_images(digit_images_path):
    digit_images = []
    for i in range(10):
        path = f"{digit_images_path}/{i}.png"
        try:
            image = pygame.image.load(path).convert_alpha()
            digit_images.append(image)
        except pygame.error as e:
            print(f"Failed to load digit image at {path}: {e}")
            sys.exit(1)
    return digit_images

print("assets loaded successfully")




'''
assets.py:

Contains functions for loading images and sounds.
Imports: pygame, sys and global_vars.py.
Then initializes w/ init() and sets the display mode.
'''