#start_game.py

import pygame
from .global_vars import config

def start_game():
    global game_over, pipes, generate_pipes, score, popup_active, bird
    print("Starting game...")  # Debug print
    if config.bird is None:
        print("Error 11: Bird is not initialized! start_game.py")  # Debug print
        return
    config.game_over = False
    config.popup_active = False
    config.pipes.clear()
    config.score = 0
    config.all_sprites.empty()
    config.pipes_group.empty()
    config.all_sprites.add(config.bird)
    config.bird.rect.y = config.HEIGHT // 2
    pygame.mixer.music.load(config.BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
    print("Game started")  # Debug print

print("start_game loaded successfully")




