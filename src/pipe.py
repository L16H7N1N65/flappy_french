#pipe.py

import pygame
import random
from global_vars import config
from thegodfather import TheGodfather
from assets import load_images, load_sounds
from start_game import start_game

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image_path, initial_position, size=None, rotate=False, speed=2):
        super().__init__()
        image = pygame.image.load(image_path)
        if size is not None:
            image = pygame.transform.scale(image, size)
        if rotate:
            image = pygame.transform.rotate(image, 180)
        self.image = image
        self.rect = self.image.get_rect(topleft=initial_position)
        self.speed = speed
        self.scored = False

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

def generate_pipes():
    global thegodfather_sound, TheGodfather
    if config.difficulty not in config.DIFFICULTIES:
        print(f"Error 28: Difficulty '{config.difficulty}' not found in DIFFICULTIES! pipe.py")
        return
    print(f"ligne 30 pipe.py difficulty = {config.difficulty}")
    gap = config.DIFFICULTIES[config.difficulty]['gap']
    pipe_speed = config.DIFFICULTIES[config.difficulty]['pipe_speed']
    last_pipe = config.pipes[-1] if config.pipes else None

    if not config.pipes or (last_pipe and last_pipe.rect.right < config.WIDTH - 300):
        pipe_height = random.randint(100, 300)
        pipe_top = Pipe(config.PIPE_IMAGE_PATH, (config.WIDTH, pipe_height - 400), size=(80, 400), rotate=True, speed=pipe_speed)
        pipe_bottom = Pipe(config.PIPE_IMAGE_PATH, (config.WIDTH, pipe_height + gap), size=(80, 400), speed=pipe_speed)
        config.pipes.extend([pipe_top, pipe_bottom])
        config.pipes_group.add(pipe_top, pipe_bottom)

        if len(config.pipes) // 2 % 4 == 0:
            thegodfather = TheGodfather(config.thegodfather_group, config.all_sprites, config.WIDTH, pipe_bottom.rect.top + pipe_bottom.rect.height)
            config.all_sprites.add(thegodfather)
            config.thegodfather_group.add(thegodfather)
            config.THEGODFATHER_SOUND.play()

    config.pipes_group.update()

    for i in range(0, len(config.pipes), 2):
        check_score(config.pipes[i], config.pipes[i + 1])

def check_score(pipe_top, pipe_bottom):
    if pipe_top is not None and pipe_bottom is not None:
        if not pipe_top.scored and pipe_top.rect.right < config.bird.rect.left:
            pipe_top.scored = pipe_bottom.scored = True
            config.score += 1
            config.bird.play_pass_pipe_sound()

def set_difficulty(difficulty_level):
    config.difficulty = difficulty_level
    if config.difficulty not in config.DIFFICULTIES:
        print(f"Error 30: Difficulty '{config.difficulty}' not found in DIFFICULTIES! pipe.py ")
        return
    print(f"Difficulty set to {config.difficulty}")  # Debug print
    start_game()

print("pipe loaded successfully")










