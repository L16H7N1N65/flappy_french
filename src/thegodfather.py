#game_over.py

import pygame
from .global_vars import config
from .fireball import Fireball
import random

class TheGodfather(pygame.sprite.Sprite):
    def __init__(self, group, all_sprites, x, y):
        super().__init__(group, all_sprites)
        self.image = pygame.image.load(config.THEGODFATHER_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (94, 110))
        self.rect = self.image.get_rect(midbottom=(x, y))  # Adjusted to be slightly left
        self.initial_y = y
        self.top = self.rect.y - 450
        self.y_change = -2
        self.timer = 0
        self.fireball_timer = 0
        self.fireball_interval = 300
        self.fireball_count = 0
        self.fireball_limit = 2
        self.sound_played = False  # Track if the sound has been played

    def update(self):
        if self.y_change != 0:
            self.rect.y += self.y_change
            if self.y_change < 0:  # water trail when ascending
                self.generate_water_trail()

            if self.rect.y <= self.top:
                self.y_change = 0
                self.timer = 90
                self.fireball_timer = pygame.time.get_ticks()
                if not self.sound_played:
                    config.THEGODFATHER_SOUND.set_volume(1.0)  # volume
                    config.THEGODFATHER_SOUND.play()
                    self.sound_played = True
        elif self.timer > 0:
            self.timer -= 1
            current_time = pygame.time.get_ticks()
            if self.fireball_count < self.fireball_limit and current_time - self.fireball_timer >= self.fireball_interval:
                fireball = Fireball(self.rect.center, self.get_fireball_direction())
                config.all_sprites.add(fireball)
                config.balls_group.add(fireball)
                self.fireball_timer = current_time
                self.fireball_count += 1

            if self.timer <= 0:
                self.y_change = 10  # Increase speed to disappear
        else:
            self.rect.y += self.y_change
            if self.rect.y >= self.initial_y:
                self.kill()

    def get_fireball_direction(self):
        bird_center_x, bird_center_y = config.bird.rect.center
        thegodfather_center_x, thegodfather_center_y = self.rect.center
        direction_x = bird_center_x - thegodfather_center_x
        direction_y = bird_center_y - thegodfather_center_y
        magnitude = (direction_x**2 + direction_y**2)**0.5
        return direction_x / magnitude, direction_y / magnitude

    def generate_water_trail(self):
        for _ in range(5):  # trail effect
            particle = Particle(self.rect.midbottom)
            config.all_sprites.add(particle)

class Particle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 191, 255))  # DeepSkyBlue color trail
        self.rect = self.image.get_rect(center=position)
        self.velocity = [random.uniform(-1, 1), random.uniform(-3, -1)]  # Random velocity
        self.gravity = 0.1

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.top > config.HEIGHT or self.rect.bottom < 0:
            self.kill()

print("thegodfather loaded successfully")







