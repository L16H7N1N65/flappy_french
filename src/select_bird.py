import pygame
from global_vars import AVATAR_BIRDS, BIRD_SIZE, BIRD_SELECT_SOUNDS, BIRD_PASS_PIPE_SOUNDS, ANIMATED_BIRDS, HEIGHT, WIDTH, current_select_sound, bird
from assets import load_images
from bird import Bird

def select_bird(index):
    global selected_bird_index, bird_image, bird, current_select_sound
    print(f"Selecting bird index: {index}")  # Debug print
    if current_select_sound:
        current_select_sound.stop()
    selected_bird_index = index
    bird_image_path = AVATAR_BIRDS[selected_bird_index]
    bird_image = pygame.image.load(bird_image_path).convert_alpha()
    bird_select_sound = pygame.mixer.Sound(BIRD_SELECT_SOUNDS[selected_bird_index])
    bird_pass_pipe_sound = pygame.mixer.Sound(BIRD_PASS_PIPE_SOUNDS[selected_bird_index])
    bird_type = f'bird{selected_bird_index + 1}'
    animated_images = load_images(ANIMATED_BIRDS.get(bird_type, [bird_image_path]), BIRD_SIZE)
    bird = Bird(animated_images, bird_image, (100, HEIGHT // 2), bird_select_sound, bird_pass_pipe_sound, bird_type)
    current_select_sound = bird_select_sound
    current_select_sound.play()
    print("Bird selected and initialized")  # Debug print

print("select_bird loaded successfully")




