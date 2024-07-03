# bird.py

import pygame
from global_vars import config
from assets import load_images, load_sounds

class Bird(pygame.sprite.Sprite):
    def __init__(self, images, avatar_image, initial_position, select_sound, pass_pipe_sound, bird_type):
        super().__init__()
        self.images = images
        self.image = pygame.transform.scale(self.images[0], (74, 94))
        self.rect = self.image.get_rect(center=initial_position)
        self.avatar_image = pygame.transform.scale(avatar_image, (50, 50))
        self.select_sound = select_sound
        self.pass_pipe_sound = pass_pipe_sound
        self.bird_type = bird_type
        self.current_image_index = 0
        self.velocity = 0
        self.gravity = 0.6
        self.jump_velocity = -8
        self.is_jumping = False
        self.animation_frame_time = 0
        self.animation_interval = 200  # milliseconds

        self.animated_images = {
            'bird1': load_images(config.ANIMATED_BIRDS['bird1'], config.BIRD_SIZE),
            'bird2': load_images(config.ANIMATED_BIRDS['bird2'], config.BIRD_SIZE),
            'bird3': load_images(config.ANIMATED_BIRDS['bird3'], config.BIRD_SIZE),
            'bird4': load_images(config.ANIMATED_BIRDS['bird4'], config.BIRD_SIZE),
        }

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
        elif self.rect.bottom >= config.HEIGHT:
            self.rect.bottom = config.HEIGHT
            self.velocity = 0

        if self.is_jumping:
            current_time = pygame.time.get_ticks()
            if current_time - self.animation_frame_time >= self.animation_interval:
                self.animate()
                self.animation_frame_time = current_time
        else:
            self.image = pygame.transform.scale(self.images[0], (74, 94))

    def jump(self):
        self.velocity = self.jump_velocity
        self.is_jumping = True

    def animate(self):
        if self.bird_type in self.animated_images:
            self.current_image_index = (self.current_image_index + 1) % len(self.animated_images[self.bird_type])
            self.image = pygame.transform.scale(self.animated_images[self.bird_type][self.current_image_index], (74, 94))

    def play_select_sound(self):
        self.select_sound.play()

    def play_pass_pipe_sound(self):
        self.pass_pipe_sound.play()

print("bird.py loaded successfully")






        
'''
defines the behavior and properties of a bird object in the game. It includes methods for the bird's movement, animation, and interactions with other game elements
'''

