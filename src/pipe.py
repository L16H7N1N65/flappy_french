import pygame
import random
from global_vars import *
from thegodfather import TheGodfather
from assets import *

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
    global pipes, difficulty, mario_sound, TheGodfather
    print(f"ligne 27 pipe.py diffficulty = {difficulty}")
    gap = DIFFICULTIES[difficulty]['gap']
    pipe_speed = DIFFICULTIES[difficulty]['pipe_speed']
    last_pipe = pipes[-1] if pipes else None

    if not pipes or (last_pipe and last_pipe.rect.right < WIDTH - 300):
        pipe_height = random.randint(100, 300)
        pipe_top = Pipe(PIPE_IMAGE_PATH, (WIDTH, pipe_height - 400), size=(80, 400), rotate=True, speed=pipe_speed)
        pipe_bottom = Pipe(PIPE_IMAGE_PATH, (WIDTH, pipe_height + gap), size=(80, 400), speed=pipe_speed)
        pipes.extend([pipe_top, pipe_bottom])
        pipes_group.add(pipe_top, pipe_bottom)

        if len(pipes) // 2 % 4 == 0:
            thegodfather = TheGodfather(thegodfather_group, all_sprites, WIDTH, pipe_bottom.rect.top + pipe_bottom.rect.height)
            all_sprites.add(thegodfather)
            thegodfather_group.add(thegodfather)
            mario_sound.play()

    pipes_group.update()

    for i in range(0, len(pipes), 2):
        check_score(pipes[i], pipes[i + 1])

def check_score(pipe_top, pipe_bottom):
    global score
    if pipe_top is not None and pipe_bottom is not None:
        if not pipe_top.scored and pipe_top.rect.right < bird.rect.left:
            pipe_top.scored = pipe_bottom.scored = True
            score += 1
            bird.play_pass_pipe_sound()

print("pipe loaded successfully")




