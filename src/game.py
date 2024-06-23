##game.py

import pygame
import random
import sys
import webbrowser
from bird import Bird
from pipe import Pipe

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (112, 197, 206)
PIPE_COLOR = (46, 213, 115)
BIRD_IMAGES = [
    '../assets/birds/bird1.png',
    '../assets/birds/bird2.png',
    '../assets/birds/bird3.png',
    '../assets/birds/bird4.png',
    '../assets/birds/bird5.png',
    '../assets/birds/bird6.png',
    '../assets/birds/bird7.png',
    '../assets/birds/bird8.png'
]
BIRD_SIZE = (74, 94)
BACKGROUND_IMAGE_PATH = '../assets/background.png'

DIFFICULTIES = {
    'easy': {'gap': 260, 'pipe_speed': 2},
    'hard': {'gap': 195, 'pipe_speed': 3},
    'advanced': {'gap': 130, 'pipe_speed': 4}
}

# Global variables
bird_images = []
bird_image = None
selected_bird_index = 0
difficulty = ''
pipes = []
score = 0
game_over = False
popup_active = False

# Blinking related variables
blink = False
last_blink_time = 0
blink_speed = 500

# Initialize Pygame
pygame.font.init()
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 15)

# Sprites
all_sprites = pygame.sprite.Group()
pipes_group = pygame.sprite.Group()

def load_images(image_paths):
    images = []
    for path in image_paths:
        try:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, BIRD_SIZE)
            images.append(image)
        except pygame.error as e:
            print(f"Failed to load image at {path}: {e}")
            sys.exit(1)
    return images

def draw_text(text, font, color, x, y, screen):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_start_screen(screen, blink):
    bg_initial = pygame.image.load("../assets/bg_initial.png")
    bg_initial_scaled = pygame.transform.scale(bg_initial, (WIDTH, HEIGHT))
    screen.blit(bg_initial_scaled, (0, 0))

    logo = pygame.image.load("../assets/logo.png")
    logo = pygame.transform.scale(logo, (logo.get_width() // 1.6, logo.get_height() // 1.6))
    logo_rect = logo.get_rect(topright=(WIDTH - 25, 18))
    screen.blit(logo, logo_rect)

    initial_start = pygame.image.load("../assets/initial_start.png")
    initial_start = pygame.transform.scale(initial_start, (initial_start.get_width() // 1.6, initial_start.get_height() // 1.6))
    initial_start_rect = initial_start.get_rect(bottomright=(WIDTH - 25, HEIGHT - 25))
    if blink:
        screen.blit(initial_start, initial_start_rect)

def draw_bird_selection_screen(screen, bird_images):
    screen.fill(BACKGROUND_COLOR)
    draw_text("Select Your Bird", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)

    button_width, button_height = 120, 60
    for i in range(len(bird_images)):
        row = i // 4
        col = i % 4
        button_x = (WIDTH // 2 - (button_width * 4 + 30) // 2) + col * (button_width + 10)
        button_y = HEIGHT // 2 + row * (button_height + 10)
        pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, button_width, button_height))
        screen.blit(pygame.transform.scale(bird_images[i], (button_width, button_height)), (button_x, button_y))
        if selected_bird_index == i:
            pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height), 3)

    start_img = pygame.image.load("../assets/start.png")
    start_img = pygame.transform.scale(start_img, (button_width, button_height))
    start_img_rect = start_img.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    screen.blit(start_img, start_img_rect)
    
def draw_game_over_screen(screen):
    global popup_active
    popup_active = True
    screen.fill(BACKGROUND_COLOR)
    draw_text("Game Over", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)
    draw_text(f"Your Score: {score}", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2, screen)
    pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 4, HEIGHT * 3 // 4 - 50, WIDTH // 2, 50))
    draw_text("About me", font_medium, (255, 255, 255), WIDTH // 2, HEIGHT * 3 // 4 - 25, screen)
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
    start_game()  # Reset game when bird is selected

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
    global screen, bird_images, clock, bird, selected_bird_index, difficulty, game_over, pipes, score, popup_active, blink, last_blink_time

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    bird_images = load_images(BIRD_IMAGES)
    selected_bird_index = 0  # default bird
    bird = Bird(bird_images, (100, HEIGHT // 2))

    # Load and scale the background image
    background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    
    background_x = 0  # Keeping track of the starting

    start_screen = True
    bird_selection_screen = False
    difficulty_screen = False
    game_running = False
    blink = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if start_screen:
                    start_screen = False
                    bird_selection_screen = True
                elif bird_selection_screen:
                    if event.key == pygame.K_LEFT:
                        selected_bird_index = (selected_bird_index - 1) % len(bird_images)
                    elif event.key == pygame.K_RIGHT:
                        selected_bird_index = (selected_bird_index + 1) % len(bird_images)
                    elif event.key == pygame.K_RETURN:
                        bird_selection_screen = False
                        difficulty_screen = True
                elif difficulty_screen:
                    if event.key == pygame.K_UP:
                        set_difficulty('easy')
                        difficulty_screen = False
                        game_running = True
                    elif event.key == pygame.K_DOWN:
                        set_difficulty('advanced')
                        difficulty_screen = False
                        game_running = True
                    elif event.key == pygame.K_RIGHT:
                        set_difficulty('hard')
                        difficulty_screen = False
                        game_running = True
                elif game_running:
                    if event.key == pygame.K_SPACE:
                        bird.jump()
                elif game_over and popup_active:
                    if event.key == pygame.K_RETURN:
                        popup_active = False
                        start_screen = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_screen:
                    start_screen = False
                    bird_selection_screen = True
                elif bird_selection_screen:
                    x, y = event.pos
                    button_width, button_height = 120, 60
                    for i in range(len(bird_images)):
                        row = i // 4
                        col = i % 4
                        button_x = (WIDTH // 2 - (button_width * 4 + 30) // 2) + col * (button_width + 10)
                        button_y = HEIGHT // 2 + row * (button_height + 10)
                        if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
                            select_bird(i)
                    start_img_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT - 100, button_width, button_height))
                    if start_img_rect.collidepoint(event.pos):
                        bird_selection_screen = False
                        difficulty_screen = True
                elif difficulty_screen:
                    easy_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 30, WIDTH // 2, 60)
                    hard_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 40, WIDTH // 2, 60)
                    advanced_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 110, WIDTH // 2, 60)
                    if easy_rect.collidepoint(event.pos):
                        set_difficulty('easy')
                        difficulty_screen = False
                        game_running = True
                    elif hard_rect.collidepoint(event.pos):
                        set_difficulty('hard')
                        difficulty_screen = False
                        game_running = True
                    elif advanced_rect.collidepoint(event.pos):
                        set_difficulty('advanced')
                        difficulty_screen = False
                        game_running = True
                elif game_over and popup_active:
                    x, y = event.pos
                    if WIDTH // 4 <= x <= WIDTH // 4 + WIDTH // 2:
                        if HEIGHT * 3 // 4 - 50 <= y <= HEIGHT * 3 // 4:
                            webbrowser.open('path_to_pdf')
                        elif HEIGHT * 3 // 4 + 10 <= y <= HEIGHT * 3 // 4 + 60:
                            start_game()
                            game_running = True
                            popup_active = False
                        elif HEIGHT * 3 // 4 + 70 <= y <= HEIGHT * 3 // 4 + 120:
                            pygame.quit()
                            sys.exit()
                        elif HEIGHT * 3 // 4 + 130 <= y <= HEIGHT * 3 // 4 + 180:
                            webbrowser.open('https://example.com')

        if start_screen:
            current_time = pygame.time.get_ticks()
            if current_time - last_blink_time >= blink_speed:
                blink = not blink
                last_blink_time = current_time
            draw_start_screen(screen, blink)
        elif bird_selection_screen:
            draw_bird_selection_screen(screen, bird_images)
        elif difficulty_screen:
            screen.fill(BACKGROUND_COLOR)
            draw_text("Select Difficulty", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)
            easy_rect = pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 4, HEIGHT // 2 - 30, WIDTH // 2, 60))
            hard_rect = pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 4, HEIGHT // 2 + 40, WIDTH // 2, 60))
            advanced_rect = pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 4, HEIGHT // 2 + 110, WIDTH // 2, 60))
            draw_text("Easy", font_medium, (0, 0, 0), easy_rect.centerx, easy_rect.centery, screen)
            draw_text("Hard", font_medium, (0, 0, 0), hard_rect.centerx, hard_rect.centery, screen)
            draw_text("Advanced", font_medium, (0, 0, 0), advanced_rect.centerx, advanced_rect.centery, screen)
        elif game_running:
            # Scroll the background image
            background_x -= 2 
            if background_x <= -WIDTH:
                background_x = 0

            screen.blit(background_image, (background_x, 0))
            screen.blit(background_image, (background_x + WIDTH, 0))

            all_sprites.update()
            all_sprites.draw(screen)
            generate_pipes(screen)

            if pygame.sprite.spritecollideany(bird, pipes_group):
                game_running = False
                game_over = True

            pygame.display.update()
        elif game_over:
            draw_game_over_screen(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

"""
#### Note my self
    
## restrain birds to a fixed sized                                       <<<<<<<<<<<< done
## Pipes logic isnt working -- to be fixed !                             <<<<<<<<<<<< done
## Create a video before after screen start                              <<<<<<<<<<<< done
## modify bird mov from mouse to keyup and keydown                       <<<<<<<<<<<< done however replaced with space bar to fly 
## redefine pop up when the game is lost                                 <<<<<<<<<<<< reverted to basics, it works but needs style 
## Birds shall be centered on start 4 x 4                                <<<<<<<<<<<< done
## Birds are still randomnly chosen when game starts        
                             
## sounds when choosing the bird                                          <<<<<<<<<<<< pending
## sounds when game is lost                                               <<<<<<<<<<<< pending
## sounds when game is won                                                <<<<<<<<<<<< pending
## sounds during game                                                     <<<<<<<<<<<< pending
## Add a score board and load the assests                                 <<<<<<<<<<<< pending
    
## background modify                                                      <<<<<<<<<<<< pending
## floor must be included                                                 <<<<<<<<<<<< pending

## Generate sounds for flap                                               <<<<<<<<<<<< pending
## Create sound when the game is lost                                     <<<<<<<<<<<< pending
## Create background                                                      <<<<<<<<<<<< pending

## Create a score board                                                   <<<<<<<<<<<< pending
## Create a pause button                                                  <<<<<<<<<<<< pending
## Create a restart button                                                <<<<<<<<<<<< done
## Create a stop button                                                   <<<<<<<<<<<< done
## Create a start button                                                  <<<<<<<<<<<< done
    
## Modify pdf by about me                                                 <<<<<<<<<<<< pending

"""
