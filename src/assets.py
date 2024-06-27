# assets.py
import pygame
import sys

pygame.init()


# Set the display mode
screen = pygame.display.set_mode((800, 600))

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

# Load avatar birds with AVATAR_SIZE
#avatar_birds = load_images(AVATAR_BIRDS, AVATAR_SIZE )


# Load bird select sounds
#bird_select_sounds = load_sounds(BIRD_SELECT_SOUNDS)
#bird_pass_pipe_sounds = load_sounds(BIRD_PASS_PIPE_SOUNDS)

print("assets loaded successfully")

'''
assets.py:

Contains functions for loading images and sounds.
Imports: pygame, sys and global_vars.py.
Then initializes w/ init() and sets the display mode.
'''