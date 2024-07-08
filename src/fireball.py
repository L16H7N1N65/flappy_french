import pygame
from src.global_vars import config

class Fireball(pygame.sprite.Sprite):
    def __init__(self, initial_position, direction):
        super().__init__()
        self.image = pygame.image.load(config.BALL_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=initial_position)
        self.speed = 10
        self.direction = direction

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if self.rect.right < 0 or self.rect.left > config.WIDTH or self.rect.top < 0 or self.rect.bottom > config.HEIGHT:
            self.kill()
        if self.rect.colliderect(config.bird.rect):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {}))
            self.kill()

