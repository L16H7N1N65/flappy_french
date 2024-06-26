# pipe.py

import pygame
from global_vars import pipes_group

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image_path, initial_position, size=None, rotate=False):
        super().__init__()
        image = pygame.image.load(image_path)
        if size is not None:
            image = pygame.transform.scale(image, size)
        if rotate:
            image = pygame.transform.rotate(image, 180)
        self.image = image
        self.rect = self.image.get_rect(topleft=initial_position)
        self.speed = 2
        self.scored = False

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

print("pipe loaded successfully")


