import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, animated_images, bird_image, position, select_sound, pass_pipe_sound, bird_type):
        super().__init__()
        self.animated_images = animated_images
        self.image = bird_image
        self.rect = self.image.get_rect(center=position)
        self.select_sound = select_sound
        self.pass_pipe_sound = pass_pipe_sound
        self.bird_type = bird_type
        self.current_image = 0
        self.animation_time = 0.1
        self.current_time = 0
        self.velocity = 0
        self.gravity = 0.5
        self.flap_power = -10

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_image = (self.current_image + 1) % len(self.animated_images)
            self.image = self.animated_images[self.current_image]
            self.rect = self.image.get_rect(center=self.rect.center)

        self.velocity += self.gravity
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = self.flap_power
        self.select_sound.play()

    def play_pass_pipe_sound(self):
        self.pass_pipe_sound.play()

print("bird loaded successfully")





