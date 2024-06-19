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
    '../assets/bird/bird1.png',
    '../assets/bird/bird2.png',
    '../assets/bird/bird3.png',
    '../assets/bird/bird4.png',
    '../assets/bird/bird5.png',
    '../assets/bird/bird6.png',
    '../assets/bird/bird7.png',
    '../assets/bird/bird8.png'
]

#def load_images(image_paths):
#    images = []
#    for path in image_paths:
#        try:
#            image = pygame.image.load(path).convert_alpha()
#            images.append(image)
#        except pygame.error as e:
#            print(f"Failed to load image at {path}: {e}")
#            sys.exit(1)
#    return images

#bird_images = load_images(BIRD_IMAGES)


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
pygame.font.init()
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 20)

# Sprites
all_sprites = pygame.sprite.Group()
pipes_group = pygame.sprite.Group()

def load_images(image_paths):
    images = []
    for path in image_paths:
        try:
            image = pygame.image.load(path).convert_alpha()
            images.append(image)
        except pygame.error as e:
            print(f"Failed to load image at {path}: {e}")
            sys.exit(1)
    return images

def draw_text(text, font, color, x, y, screen):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_start_screen(screen):
    screen.fill(BACKGROUND_COLOR)
    draw_text("Welcome to Flappy French", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)
    draw_text("Please accept the usage conditions", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2, screen)
    draw_text("Press SPACE to continue", font_small, (0, 0, 0), WIDTH // 2, HEIGHT * 3 // 4, screen)

def draw_bird_selection_screen(screen, bird_images):
    screen.fill(BACKGROUND_COLOR)
    draw_text("Select Your Bird", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)

    button_width, button_height = 120, 60
    button_x = WIDTH // 2 - (button_width * 4) // 2
    button_y = HEIGHT // 2
    for i in range(len(bird_images)):
        pygame.draw.rect(screen, (255, 255, 255), (button_x + i * button_width, button_y, button_width, button_height))
        screen.blit(pygame.transform.scale(bird_images[i], (button_width, button_height)), (button_x + i * button_width, button_y))
        if selected_bird_index == i:
            pygame.draw.rect(screen, (255, 0, 0), (button_x + i * button_width, button_y, button_width, button_height), 3)

def draw_game_over_screen(screen):
    global popup_active
    popup_active = True
    screen.fill(BACKGROUND_COLOR)
    draw_text("Game Over", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)
    draw_text(f"Your Score: {score}", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2, screen)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 - 50, WIDTH // 2, 50))
    draw_text("Download PDF", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 - 25, screen)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 + 10, WIDTH // 2, 50))
    draw_text("Play Again", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 + 35, screen)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 + 70, WIDTH // 2, 50))
    draw_text("Stop Game", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 + 95, screen)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 + 130, WIDTH // 2, 50))
    draw_text("Visit Website", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 + 155, screen)

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

def generate_pipes(screen):
    gap = DIFFICULTIES[difficulty]['gap']
    pipe_speed = DIFFICULTIES[difficulty]['pipe_speed']
    last_pipe = pipes[-1] if pipes else None

    if not pipes or (last_pipe and last_pipe.rect.right < WIDTH - 300):
        pipe_height = random.randint(100, 300)
        pipe_top = Pipe(pygame.Surface((80, pipe_height)), (WIDTH, 0))
        pipe_bottom = Pipe(pygame.Surface((80, HEIGHT - pipe_height - gap)), (WIDTH, pipe_height + gap))
        pipes.extend([pipe_top, pipe_bottom])
        pipes_group.add(pipe_top, pipe_bottom)

    pipes_group.update()
    pipes_group.draw(screen)

def main():
    global bird_images, screen, clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    bird_images = load_images(BIRD_IMAGES)
    bird = Bird(bird_images, (100, HEIGHT // 2))

    start_screen = True
    bird_selection_screen = False
    difficulty_screen = False
    game_running = False

    while True:
        if start_screen:
            draw_start_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    start_screen = False
                    bird_selection_screen = True

        elif bird_selection_screen:
            draw_bird_selection_screen(screen, bird_images)
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
            draw_text("Select Difficulty", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)
            button_width, button_height = 200, 60
            for idx, level in enumerate(DIFFICULTIES.keys()):
                button_x = WIDTH // 2 - button_width // 2
                button_y = HEIGHT // 2 + idx * (button_height + 20)
                pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
                draw_text(level.capitalize(), font_medium, (255, 255, 255), WIDTH // 2, button_y + button_height // 2, screen)

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
                            game_running = True

        elif game_running:
            screen.fill(BACKGROUND_COLOR)
            all_sprites.update()
            all_sprites.draw(screen)
            generate_pipes(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.jump()

            if pygame.sprite.spritecollideany(bird, pipes_group):
                game_running = False
                game_over = True

        elif game_over and popup_active:
            draw_game_over_screen(screen)
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
    
    ## Note my self 
    ## restrain birds to a fixed sized 
    ## Pipes logic isnt working -- to be fixed !
    ## Add button to be checked for warnings about usages and conditions
    ## modify bird mov from mouse to keyup and keydown 
    ## redefine pop up when the game is lost 
    ## Birds shall be centered on start 4 x 4
    ## Generate sounds for flap and >>
    ## Create sound when the game is lost 
    ## Create background 
    
    