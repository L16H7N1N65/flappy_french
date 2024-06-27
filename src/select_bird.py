import pygame
from global_vars import *
from assets import load_images, load_sounds
from bird import Bird

def select_bird(index, bird_select_sounds, bird_pass_pipe_sounds, ANIMATED_BIRDS, AVATAR_BIRDS):
    global selected_bird_index, bird_image, bird, current_select_sound
    
    # Stop the current select sound if it is playing
    if current_select_sound:
        current_select_sound.stop()
        print("Stopped current select sound")

    # Update selected bird index
    selected_bird_index = index
    print(f"Selected bird index updated to {selected_bird_index}")

    # Load bird select sounds
    bird_select_sounds = load_sounds(BIRD_SELECT_SOUNDS)
    bird_pass_pipe_sounds = load_sounds(BIRD_PASS_PIPE_SOUNDS)
    print("Loaded bird select and pass pipe sounds")

    # Update current select sound
    bird_select_sound = bird_select_sounds[selected_bird_index]
    bird_pass_pipe_sound = bird_pass_pipe_sounds[selected_bird_index]
    current_select_sound = bird_select_sound
    print(f"Updated sounds for bird index {selected_bird_index}")

    # Load bird image
    bird_image_path = AVATAR_BIRDS[selected_bird_index]
    bird_image = pygame.image.load(bird_image_path).convert_alpha()
    print(f"Loaded bird image from {bird_image_path}")

    # Load animated images for bird
    bird_type = f'bird{selected_bird_index + 1}'
    animated_images = load_images(ANIMATED_BIRDS.get(bird_type, [bird_image_path]), BIRD_SIZE)
    print(f"Loaded animated images for {bird_type}")

    # Create bird instance
    bird = Bird(animated_images, bird_image, (100, HEIGHT // 2), bird_select_sound, bird_pass_pipe_sound, bird_type)
    print(f"Created bird instance for {bird_type}")

    # Play the current select sound
    current_select_sound.play()
    print("Playing current select sound")

    print(f"Bird selected: {bird_type}")

print("select_bird.py loaded successfully")




