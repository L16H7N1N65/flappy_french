## bird.py

import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, images, initial_position):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=initial_position)
        self.velocity = 0

    def update(self):
        self.velocity += 0.3  # Apply gravity
        self.rect.y += self.velocity

        # Limit bird's y position within screen boundaries
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
        elif self.rect.bottom >= 600:  # Assuming screen height is 600
            self.rect.bottom = 600
            self.velocity = 0

    def jump(self):
        self.velocity = -6  # Bird jumps

    def animate(self):
        # Animate bird's wings
        self.image = self.images[(pygame.time.get_ticks() // 100) % len(self.images)]
