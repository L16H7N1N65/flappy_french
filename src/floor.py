import pygame
from global_vars import WIDTH, HEIGHT

class Floor(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(bottomleft=(0, HEIGHT))

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < WIDTH:
            self.rect.left = 0
