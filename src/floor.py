# floor.py

import pygame

class Floor:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.height = self.image.get_height() // 5
        self.image = pygame.transform.scale(self.image, (screen_width, self.height))
        self.x = 0
        self.y = screen_height - self.height

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + self.image.get_width(), self.y))

    def update(self):
        self.x -= 2
        if self.x <= -self.image.get_width():
            self.x = 0
