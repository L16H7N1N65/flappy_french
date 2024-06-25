import pygame
from global_vars import AVATAR_BIRDS, BIRD_SIZE, BIRD_SELECT_SOUNDS, BIRD_PASS_PIPE_SOUNDS, ANIMATED_BIRDS
from load_images import load_images
from bird import Bird

def select_bird(index):
    global selected_bird_index, bird_image, bird, current_select_sound
    if current_select_sound:
        current_select_sound.stop()
    selected_bird_index = index
    bird_image_path = AVATAR_BIRDS[selected_bird_index]  # Get the path
    bird_image = pygame.image.load(bird_image_path).convert_alpha()  # Load the image as a surface
    bird_select_sound = BIRD_SELECT_SOUNDS[selected_bird_index]
    bird_pass_pipe_sound = BIRD_PASS_PIPE_SOUNDS[selected_bird_index]
    bird_type = f'bird{selected_bird_index + 1}'
    animated_images = load_images(ANIMATED_BIRDS.get(bird_type, [bird_image_path]), BIRD_SIZE)
    bird = Bird(animated_images, bird_image, (100, HEIGHT // 2), bird_select_sound, bird_pass_pipe_sound, bird_type)
    current_select_sound = bird_select_sound
    current_select_sound.play()
