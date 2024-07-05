import pygame
from global_vars import config
from assets import load_images, load_sounds
from bird import Bird
from font import draw_text

def select_bird(index):
    global bird

    # Stop the current select sound if it is playing
    if config.current_select_sound:
        config.current_select_sound.stop()
        print("Stopped current select sound")

    # Update selected bird index
    config.selected_bird_index = index
    print(f"Selected bird index updated to {config.selected_bird_index}")

    # Load bird select sounds
    bird_select_sounds = load_sounds(config.BIRD_SELECT_SOUNDS)
    bird_pass_pipe_sounds = load_sounds(config.BIRD_PASS_PIPE_SOUNDS)
    print("Loaded bird select and pass pipe sounds")

    # Update current select sound
    bird_select_sound = bird_select_sounds[config.selected_bird_index]
    bird_pass_pipe_sound = bird_pass_pipe_sounds[config.selected_bird_index]
    config.current_select_sound = bird_select_sound
    print(f"Updated sounds for bird index {config.selected_bird_index}")

    # Load bird image
    bird_image_path = config.AVATAR_BIRDS[config.selected_bird_index]
    bird_image = pygame.image.load(bird_image_path).convert_alpha()
    print(f"Loaded bird image from {bird_image_path}")

    # Load animated images for bird
    bird_type = f'bird{config.selected_bird_index + 1}'
    animated_images = load_images(config.ANIMATED_BIRDS.get(bird_type, [bird_image_path]), config.BIRD_SIZE)
    print(f"Loaded animated images for {bird_type}")

    # Create bird instance
    bird = Bird(animated_images, bird_image, (100, config.HEIGHT // 2), bird_select_sound, bird_pass_pipe_sound, bird_type)
    config.bird = bird
    print(f"Created bird instance for {bird_type}")

    # Play the current select sound
    config.current_select_sound.play()
    print("Playing current select sound")

    print(f"Bird selected: {bird}")

    return bird

def draw_bird_selection_screen(screen, avatar_birds):
    screen.fill(config.BACKGROUND_COLOR)
    draw_text("Qui sera ton candidat ?", config.font_large, (0, 0, 0), config.WIDTH // 2, config.HEIGHT // 4, screen)

    button_width, button_height = 120, 60
    for i in range(len(avatar_birds)):
        row = i // 4
        col = i % 4
        button_x = (config.WIDTH // 2 - (button_width * 4 + 30) // 2) + col * (button_width + 10)
        button_y = config.HEIGHT // 2 + row * (button_height + 10)
        
        # Draw the bird button
        pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, button_width, button_height))
        screen.blit(avatar_birds[i], (button_x + 35, button_y + 5))
        
        # Draw red rectangle if this is the selected bird
        if config.selected_bird_index == i:
            pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height), 3)

    # Draw the start button
    start_img = pygame.image.load(config.START_IMAGE_PATH)
    start_img = pygame.transform.scale(start_img, (button_width, button_height))
    start_img_rect = start_img.get_rect(center=(config.WIDTH // 2, config.HEIGHT - 100))
    screen.blit(start_img, start_img_rect)
    return start_img_rect

print("select_bird.py loaded successfully")









'''
fn responsible for selecting a bird from a list of available birds. It handles the logic for updating the selected bird, loading the corresponding images and sounds, and creating an instance of the Bird class with the selected attributes
'''




