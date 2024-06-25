## pipe.py

import pygame
from global_vars import PIPE_IMAGE_PATH

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size=(80, 400), rotate=False):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        if rotate:
            self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(topleft=position)
        self.scored = False

    def update(self):
        self.rect.x -= 2
        if self.rect.right < 0:
            self.kill()



    """
    Note to myself:
    
    Replace generated pipes by png loaded in assets folder
    
    """