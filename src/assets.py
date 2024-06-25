# assets.py
import pygame
import sys

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

print("assets loaded successfully")
