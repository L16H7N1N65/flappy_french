import pygame
import random
import sys
import webbrowser
import os

# Initialize Pygame
pygame.init()

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

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load bird images
bird_images = []
for bird_file in BIRD_IMAGES:
    # Use os.path.join to construct the correct path
    bird_images.append(pygame.image.load(os.path.join(os.path.dirname(__file__), bird_file)))

# Select initial bird
bird_image = bird_images[selected_bird_index]

# Clock for controlling FPS
clock = pygame.time.Clock()

# Fonts
pygame.font.init()
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 20)

# Functions
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_start_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_text("Welcome to Flappy Bird", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4)
    draw_text("Please accept the usage conditions", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2)
    draw_text("Press SPACE to continue", font_small, (0, 0, 0), WIDTH // 2, HEIGHT * 3 // 4)

def draw_bird_selection_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_text("Select Your Bird", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4)
    
    # Draw bird options
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
    generate_pipes()
    bird.y = HEIGHT // 2

def select_bird(index):
    global selected_bird_index, bird_image
    selected_bird_index = index
    bird_image = bird_images[selected_bird_index]

def set_difficulty(level):
    global difficulty
    difficulty = level
    start_game()

def generate_pipes():
    global pipes
    gap = DIFFICULTIES[difficulty]['gap']
    pipe_speed = DIFFICULTIES[difficulty]['pipe_speed']
    timer = 0
    while not game_over:
        pipe_height = random.randint(50, HEIGHT - gap - 50)
        pipes.append({'x': WIDTH, 'y': pipe_height, 'height': gap})
        pipes.append({'x': WIDTH, 'y': pipe_height + gap, 'height': HEIGHT - pipe_height - gap})

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not popup_active:
                    bird_jump()

        bird_rect = bird_image.get_rect(topleft=(bird.x, bird.y))
        for pipe in pipes:
            top_pipe_rect = pygame.Rect(pipe['x'], 0, 50, pipe['height'])
            bottom_pipe_rect = pygame.Rect(pipe['x'], pipe['y'], 50, HEIGHT - pipe['y'])
            if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
                draw_game_over_screen()
                return True
            pipe['x'] -= pipe_speed
            if pipe['x'] <= -50:
                pipes.remove(pipe)

        draw_game()

def bird_jump():
    bird.velocity = -6

# Main game loop
while True:
    if not difficulty:
        draw_start_screen()
    elif not bird_image:
        draw_bird_selection_screen()
    elif not game_over and not popup_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_jump()

        bird.velocity += 0.3
        bird.y += bird.velocity

        if bird.y < 0:
            bird.y = 0
            bird.velocity = 0
        elif bird.y > HEIGHT - bird_image.get_height():
            bird.y = HEIGHT - bird_image.get_height()
            bird.velocity = 0

        screen.fill(BACKGROUND_COLOR)

        # Draw pipes
        for pipe in pipes:
            pygame.draw.rect(screen, PIPE_COLOR, (pipe['x'], 0, 50, pipe['height']))
            pygame.draw.rect(screen, PIPE_COLOR, (pipe['x'], pipe['y'], 50, HEIGHT - pipe['y']))

            if pipe['x'] == 50:
                score += 1

        # Draw bird
        screen.blit(bird_image, (bird.x, bird.y))

        # Draw score
        draw_text(f"Score: {score}", font_medium, (0, 0, 0), WIDTH // 2, 50)

        # Update pipes position
        for pipe in pipes:
            pipe['x'] -= 2

        # Check collision
        bird_rect = bird_image.get_rect(topleft=(bird.x, bird.y))
        for pipe in pipes:
            top_pipe_rect = pygame.Rect(pipe['x'], 0, 50, pipe['height'])
            bottom_pipe_rect = pygame.Rect(pipe['x'], pipe['y'], 50, HEIGHT - pipe['y'])
            if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
                draw_game_over_screen()
                game_over = True

        pygame.display.update()
        clock.tick(60)

    elif game_over and popup_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Download PDF option
                if WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 - 50 <= mouse_y <= HEIGHT * 3 // 4:
                    print("Download PDF")
                    # Example: open a PDF file
                    webbrowser.open_new("https://www.linkedin.com/feed/update/urn:li:activity:7205913460470136832/")
                # Play again option
                elif WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 + 10 <= mouse_y <= HEIGHT * 3 // 4 + 60:
                    print("Play Again")
                    start_game()
                # Stop game option
                elif WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 + 70 <= mouse_y <= HEIGHT * 3 // 4 + 120:
                    print("Stop Game")
                    pygame.quit()
                    sys.exit()
                # Visit website option
                elif WIDTH // 4 <= mouse_x <= WIDTH // 4 + WIDTH // 2 and HEIGHT * 3 // 4 + 130 <= mouse_y <= HEIGHT * 3 // 4 + 180:
                    print("Visit Website")
                    webbrowser.open_new("https://www.service-public.fr/particuliers/vosdroits/F1943")
                else:
                    popup_active = False

        pygame.display.update()
        clock.tick(60)

pygame.quit()

