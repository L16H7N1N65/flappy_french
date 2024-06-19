import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, initial_position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=initial_position)
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed

        # Add logic to reset position or re-generate pipes off-screen
