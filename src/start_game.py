import pygame
from global_vars import all_sprites, pipes_group, bird, BACKGROUND_MUSIC_PATH, HEIGHT

def start_game():
    global game_over, pipes, score, popup_active
    game_over = False
    popup_active = False
    pipes = []
    score = 0
    all_sprites.empty()
    pipes_group.empty()
    all_sprites.add(bird)
    bird.rect.y = HEIGHT // 2
    pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)  # Play the background music in a loop
