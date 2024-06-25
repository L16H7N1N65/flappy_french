import pygame
from fireball import Fireball
from global_vars import WIDTH, HEIGHT, bird, all_sprites, balls_group

class TheGodfather(pygame.sprite.Sprite):
    def __init__(self, group, all_sprites, x, y):
        super().__init__(group, all_sprites)
        self.image = pygame.image.load("../assets/birds/mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (94, 110))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.initial_y = y
        self.counter = 0
        self.top = self.rect.y - 250
        self.y_change = -2
        self.timer = 0
        self.fireball_timer = 0
        self.fireball_interval = 1000
        self.fireball_count = 0
        self.fireball_limit = 5
        self.direction = -1

    def update(self):
        if self.timer <= 0:
            if self.rect.y <= self.top:
                self.y_change = 0
                self.timer = 90
                self.fireball_timer = pygame.time.get_ticks()
            self.rect.y += self.y_change
        else:
            self.timer -= 1
            current_time = pygame.time.get_ticks()
            if self.fireball_count < self.fireball_limit and current_time - self.fireball_timer >= self.fireball_interval:
                fireball = Fireball(self.rect.center, self.get_fireball_direction())
                all_sprites.add(fireball)
                balls_group.add(fireball)
                self.fireball_timer = current_time
                self.fireball_count += 1

            if self.timer <= 0:
                self.y_change = 2
                if self.rect.y >= self.initial_y:
                    self.kill()

    def get_fireball_direction(self):
        bird_center_x, bird_center_y = bird.rect.center
        godfather_center_x, godfather_center_y = self.rect.center
        direction_x = bird_center_x - godfather_center_x
        direction_y = bird_center_y - godfather_center_y
        magnitude = (direction_x**2 + direction_y**2)**0.5
        return direction_x / magnitude, direction_y / magnitude
