##game.py

import pygame
import random
import sys
import webbrowser
from bird import Bird
from pipe import Pipe

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (112, 197, 206)  # light blue
PIPE_COLOR = (46, 213, 115)  # green
BIRD_IMAGES = [
    'assets/bird/bird1.png',
    'assets/bird/bird2.png',
    'assets/bird/bird3.png',
    'assets/bird/bird4.png',
    'assets/bird/bird5.png',
    'assets/bird/bird6.png',
    'assets/bird/bird7.png',
    'assets/bird/bird8.png'
]
DIFFICULTIES = {
    'easy': {'gap': 260, 'pipe_speed': 2},
    'hard': {'gap': 195, 'pipe_speed': 3},
    'advanced': {'gap': 130, 'pipe_speed': 4}
}

# Global variables
bird_image = None
selected_bird_index = 0
difficulty = ''
pipes = []
score = 0
game_over = False
popup_active = False

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy French')
clock = pygame.time.Clock()

# Load bird images
bird_images = [pygame.image.load(img) for img in BIRD_IMAGES]

# Fonts
pygame.font.init()
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 20)

# Sprites
all_sprites = pygame.sprite.Group()
pipes_group = pygame.sprite.Group()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_start_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_text("Welcome to Flappy French", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4)
    draw_text("Please accept the usage conditions", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2)
    draw_text("Press SPACE to continue", font_small, (0, 0, 0), WIDTH // 2, HEIGHT * 3 // 4)

def draw_bird_selection_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_text("Select Your Bird", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4)

    button_width, button_height = 120, 60
    button_x = WIDTH // 2 - (button_width * 4) // 2
    button_y = HEIGHT // 2
    for i in range(len(bird_images)):
        pygame.draw.rect(screen, (255, 255, 255), (button_x + i * button_width, button_y, button_width, button_height))
        screen.blit(pygame.transform.scale(bird_images[i], (button_width, button_height)), (button_x + i * button_width, button_y))
        if selected_bird_index == i:
            pygame.draw.rect(screen, (255, 0, 0), (button_x + i * button_width, button_y, button_width, button_height), 3)

def draw_game_over_screen():
    global popup_active
    popup_active = True
    screen.fill(BACKGROUND_COLOR)
    draw_text("Game Over", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4)
    draw_text(f"Your Score: {score}", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 - 50, WIDTH // 2, 50))
    draw_text("Download PDF", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 - 25)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 + 10, WIDTH // 2, 50))
    draw_text("Play Again", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 + 35)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 + 70, WIDTH // 2, 50))
    draw_text("Stop Game", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 + 95)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 + 130, WIDTH // 2, 50))
    draw_text("Visit Website", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 + 155)

def start_game():
    global game_over, pipes, score, popup_active
    game_over = False
    popup_active = False
    pipes = []
    score = 0
    bird.rect.y = HEIGHT // 2
    all_sprites.empty()
    pipes_group.empty()
    all_sprites.add(bird)

def select_bird(index):
    global selected_bird_index, bird_image, bird
    selected_bird_index = index
    bird_image = bird_images[selected_bird_index]
    bird = Bird(bird_images, (100, HEIGHT // 2))

def set_difficulty(level):
    global difficulty
    difficulty = level
    start_game()

def generate_pipes():
    gap = DIFFICULTIES[difficulty]['gap']
    pipe_speed = DIFFICULTIES[difficulty]['pipe_speed']
    pipe_frequency = 1500  # Frequency in milliseconds
    last_pipe_time = pygame.time.get_ticks() - pipe_frequency

    while not game_over:
        current_time = pygame.time.get_ticks()
        if current_time - last_pipe_time >= pipe_frequency:
            pipe_height = random.randint(50, HEIGHT - gap - 50)
            top_pipe_image = pygame.Surface((50, pipe_height))
            top_pipe_image.fill(PIPE_COLOR)
            bottom_pipe_image = pygame.Surface((50, HEIGHT - pipe_height - gap))
            bottom_pipe_image.fill(PIPE_COLOR)
            top_pipe = Pipe(top_pipe_image, (WIDTH, 0))
            bottom_pipe = Pipe(bottom_pipe_image, (WIDTH, pipe_height + gap))
            pipes_group.add(top_pipe)
            pipes_group.add(bottom_pipe)
            all_sprites.add(top_pipe)
            all_sprites.add(bottom_pipe)
            last_pipe_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not popup_active:
                    bird.jump()

        all_sprites.update()
        
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)

        bird_rect = bird.image.get_rect(topleft=(bird.rect.x, bird.rect.y))
        if pygame.sprite.spritecollideany(bird, pipes_group):
            draw_game_over_screen()
            return True

        draw_text(f"Score: {score}", font_medium, (0, 0, 0), WIDTH // 2, 50)
        pygame.display.flip()
        clock.tick(60)

def main():
    global game_over, bird

    bird = Bird(bird_images, (100, HEIGHT // 2))
    screen.fill(BACKGROUND_COLOR)

    # Main game loop
    start_screen = True
    bird_selection_screen = False
    difficulty_screen = False

    while True:
        if start_screen:
            draw_start_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_screen = False
                        bird_selection_screen = True

        elif bird_selection_screen:
            draw_bird_selection_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_width, button_height = 120, 60
                    button_x = WIDTH // 2 - (button_width * 4) // 2
                    button_y = HEIGHT // 2
                    for i in range(len(bird_images)):
                        if button_x + i * button_width <= mouse_x <= button_x + (i + 1) * button_width and button_y <= mouse_y <= button_y + button_height:
                            select_bird(i)
                            bird_selection_screen = False
                            difficulty_screen = True

        elif difficulty_screen:
            screen.fill(BACKGROUND_COLOR)
            draw_text("Select Difficulty", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4)
            button_width, button_height = 200, 60
            for idx, level in enumerate(DIFFICULTIES.keys()):
                button_x = WIDTH // 2 - button_width // 2
                button_y = HEIGHT // 2 + idx * (button_height + 20)
                pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
                draw_text(level.capitalize(), font_medium, (255, 255, 255), WIDTH // 2, button_y + button_height // 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for idx, level in enumerate(DIFFICULTIES.keys()):
                        button_x = WIDTH // 2 - button_width // 2
                        button_y = HEIGHT // 2 + idx * (button_height + 20)
                        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                            set_difficulty(level)
                            difficulty_screen = False

        elif not game_over:
            generate_pipes()

        elif game_over and popup_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 - 50 <= mouse_y <= HEIGHT * 3 // 4:
                        webbrowser.open_new("https://www.linkedin.com/feed/update/urn:li:activity:7205913460470136832/")
                    elif WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 + 10 <= mouse_y <= HEIGHT * 3 // 4 + 60:
                        start_game()
                    elif WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 + 70 <= mouse_y <= HEIGHT * 3 // 4 + 120:
                        pygame.quit()
                        sys.exit()
                    elif WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 + 130 <= mouse_y <= HEIGHT * 3 // 4 + 180:
                        webbrowser.open_new("https://www.service-public.fr/particuliers/vosdroits/F1943")
                    else:
                        popup_active = False

        pygame.display.update()
        clock.tick(60)

pygame.quit()
