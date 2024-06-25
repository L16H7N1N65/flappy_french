import pygame
from global_vars import WIDTH, HEIGHT, bird

class Fireball(pygame.sprite.Sprite):
    def __init__(self, initial_position, direction):
        super().__init__()
        self.image = pygame.image.load("../assets/birds/ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect(center=initial_position)
        self.speed = 5
        self.direction = direction

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.kill()
        if self.rect.colliderect(bird.rect):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {}))
            self.kill()
