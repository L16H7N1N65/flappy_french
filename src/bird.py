# bird.py

import pygame
from global_vars import BIRD_SIZE, ANIMATED_BIRDS
from assets import load_images, load_sounds  # Issue here 

class Bird(pygame.sprite.Sprite):
    def __init__(self, images, avatar_image, initial_position, select_sound, pass_pipe_sound, bird_type):
        super().__init__()
        self.images = images
        self.image = pygame.transform.scale(self.images[0], (74, 94))
        self.rect = self.image.get_rect(center=initial_position)
        self.avatar_image = pygame.transform.scale(avatar_image, (50, 50))
        #
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

        # Load alternate images for specific bird types
        self.alternate_images = {
            'bird1': load_images(['../assets/birds/bird1_flap.png', '../assets/birds/bird1_flop.png'], BIRD_SIZE),
            'bird3': load_images(['../assets/birds/bird3_flap.png', '../assets/birds/bird3_flop.png'], BIRD_SIZE),
            'bird4': load_images(['../assets/birds/bird4_flap.png', '../assets/birds/bird4_flop.png'], BIRD_SIZE),
        }

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
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
        if self.bird_type in self.alternate_images:
            self.current_image_index = (self.current_image_index + 1) % len(self.alternate_images[self.bird_type])
            self.image = pygame.transform.scale(self.alternate_images[self.bird_type][self.current_image_index], (74, 94))

    def play_select_sound(self):
        self.select_sound.play()

    def play_pass_pipe_sound(self):
        self.pass_pipe_sound.play()



