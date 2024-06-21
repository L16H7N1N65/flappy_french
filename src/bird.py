import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, images, initial_position):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=initial_position)
        self.velocity = 0
        self.gravity = 0.9
        self.jump_velocity = -10

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity = 0

        self.animate()

    def jump(self):
        self.velocity = self.jump_velocity

    def animate(self):
        self.image = self.images[(pygame.time.get_ticks() // 100) % len(self.images)]
        



