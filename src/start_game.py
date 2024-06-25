import pygame
from global_vars import all_sprites, pipes_group, bird, BACKGROUND_MUSIC_PATH, HEIGHT

def start_game():
    global game_over, pipes, score, popup_active, bird
    print("Starting game...")  # Debug print
    if bird is None:
        print("Error: Bird is not initialized!")  # Debug print
        return
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
    pygame.mixer.music.play(-1)
    print("Game started")  # Debug print

print("start_game loaded successfully")

