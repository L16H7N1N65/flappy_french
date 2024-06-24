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
AVATAR_BIRDS = [
    '../assets/birds/bird1.png',
    '../assets/birds/bird2.png',
    '../assets/birds/bird3.png',
    '../assets/birds/bird4.png',
    '../assets/birds/bird5.png',
    '../assets/birds/bird6.png',
    '../assets/birds/bird7.png',
    '../assets/birds/bird8.png'
]
ANIMATED_BIRDS = {
    'bird1': [
        '../assets/birds/bird1_flap.png',
        '../assets/birds/bird1_flop.png'
    ],
    'bird2': [
        '../assets/birds/bird3_flap.png',
        '../assets/birds/bird3_flop.png'
    ],
    'bird3': [
        '../assets/birds/bird3_flap.png',
        '../assets/birds/bird3_flop.png'
    ],
    'bird4': [
        '../assets/birds/bird4_flap.png',
        '../assets/birds/bird4_flop.png'
    ],
}

AVATAR_SIZE = (45, 60)  # Adjusted avatar size
BIRD_SIZE = (77, 107)  # One-fourth of the original size
BACKGROUND_IMAGE_PATH = '../assets/background.png'
PIPE_IMAGE_PATH = '../assets/pipes/pipe.png'
DIGIT_IMAGES_PATH = '../assets/digits'

BIRD_SELECT_SOUNDS = [
    '../assets/sounds/select1.wav',
    '../assets/sounds/select2.wav',
    '../assets/sounds/select3.wav',
    '../assets/sounds/select4.wav',
    '../assets/sounds/select5.wav',
    '../assets/sounds/select6.wav',
    '../assets/sounds/select7.wav',
    '../assets/sounds/select8.wav'
]

BIRD_PASS_PIPE_SOUNDS = [
    '../assets/sounds/pass_pipe1.wav',
    '../assets/sounds/pass_pipe2.wav',
    '../assets/sounds/pass_pipe3.wav',
    '../assets/sounds/pass_pipe4.wav',
    '../assets/sounds/pass_pipe5.wav',
    '../assets/sounds/pass_pipe6.wav',
    '../assets/sounds/pass_pipe7.wav',
    '../assets/sounds/pass_pipe8.wav'
]

MARIO_SOUND = '../assets/sounds/mario.wav'
MARIO_IMAGE_PATH = '../assets/birds/mario.png'
BALL_IMAGE_PATH = '../assets/birds/ball.png'

BACKGROUND_MUSIC_PATH = '../assets/sounds/background_music.mp3'

DIFFICULTIES = {
    'easy': {'gap': 260, 'pipe_speed': 2},
    'hard': {'gap': 195, 'pipe_speed': 3},
    'advanced': {'gap': 130, 'pipe_speed': 4}
}

# Global variables
avatar_birds = []
bird_select_sounds = []
bird_pass_pipe_sounds = []
bird_image = None
selected_bird_index = 0
difficulty = ''
pipes = []
score = 0
game_over = False
popup_active = False
current_select_sound = None

# Blinking related variables
blink = False
last_blink_time = 0
blink_speed = 500

# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 15)

# Sprites
all_sprites = pygame.sprite.Group()
pipes_group = pygame.sprite.Group()
mario_group = pygame.sprite.Group()
balls_group = pygame.sprite.Group()

def load_images(image_paths, size):
    images = []
    for path in image_paths:
        try:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, size)
            images.append(image)
        except pygame.error as e:
            print(f"Failed to load image at {path}: {e}")
            sys.exit(1)
    return images

def load_sounds(sound_paths):
    sounds = []
    for path in sound_paths:
        try:
            sound = pygame.mixer.Sound(path)
            sounds.append(sound)
        except pygame.error as e:
            print(f"Failed to load sound at {path}: {e}")
            sys.exit(1)
    return sounds

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
    draw_text("Qui sera ton candidat ?", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)

    button_width, button_height = 120, 60 # Tommorrow adjust the size of the button
    for i in range(len(bird_images)):
        row = i // 4
        col = i % 4
        button_x = (WIDTH // 2 - (button_width * 4 + 30) // 2) + col * (button_width + 10)
        button_y = HEIGHT // 2 + row * (button_height + 10)
        pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, button_width, button_height))
        screen.blit(bird_images[i], (button_x + 35, button_y + 5))
        if selected_bird_index == i:
            pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height), 3)

    start_img = pygame.image.load("../assets/start.png")
    start_img = pygame.transform.scale(start_img, (button_width, button_height))
    start_img_rect = start_img.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    screen.blit(start_img, start_img_rect)

def draw_game_over_screen(screen):
    global popup_active
    popup_active = True
    pygame.mixer.music.stop()  # Stop the music when the game is over
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
    global game_over, pipes, score, popup_active, bird
    game_over = False
    popup_active = False
    pipes = []
    score = 0
    all_sprites.empty()
    pipes_group.empty()
    all_sprites.add(bird)
    bird.rect.y = HEIGHT // 2
    pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.set_volume(0.1) 
    pygame.mixer.music.play(-1) # Play the background music in a loop

def select_bird(index):
    global selected_bird_index, bird_image, bird, current_select_sound
    if current_select_sound:
        current_select_sound.stop()
    selected_bird_index = index
    bird_image = avatar_birds[selected_bird_index]
    bird_select_sound = bird_select_sounds[selected_bird_index]
    bird_pass_pipe_sound = bird_pass_pipe_sounds[selected_bird_index]
    bird_type = f'bird{selected_bird_index + 1}'
    animated_images = load_images(ANIMATED_BIRDS.get(bird_type, [bird_image]), BIRD_SIZE)
    bird = Bird(animated_images, bird_image, (100, HEIGHT // 2), bird_select_sound, bird_pass_pipe_sound, bird_type)
    current_select_sound = bird_select_sound
    current_select_sound.play()

def set_difficulty(level):
    global difficulty
    difficulty = level
    start_game()

def generate_pipes(screen):
    global mario_timer
    gap = DIFFICULTIES[difficulty]['gap']
    pipe_speed = DIFFICULTIES[difficulty]['pipe_speed']
    last_pipe = pipes[-1] if pipes else None

    if not pipes or (last_pipe and last_pipe.rect.right < WIDTH - 300):
        pipe_height = random.randint(100, 300)
        pipe_top = Pipe(PIPE_IMAGE_PATH, (WIDTH, pipe_height - 400), size=(80, 400), rotate=True)
        pipe_bottom = Pipe(PIPE_IMAGE_PATH, (WIDTH, pipe_height + gap), size=(80, 400))
        pipes.extend([pipe_top, pipe_bottom])
        pipes_group.add(pipe_top, pipe_bottom)

        if len(pipes) // 2 % 4 == 0:
            mario = Mario(mario_group, all_sprites, WIDTH, pipe_bottom.rect.top + pipe_bottom.rect.height)
            all_sprites.add(mario)
            mario_group.add(mario)
            mario_sound.play()

    pipes_group.update()
    pipes_group.draw(screen)


def load_digit_images():
    digit_images = []
    for i in range(10):
        path = f"{DIGIT_IMAGES_PATH}/{i}.png"
        try:
            image = pygame.image.load(path).convert_alpha()
            digit_images.append(image)
        except pygame.error as e:
            print(f"Failed to load digit image at {path}: {e}")
            sys.exit(1)
    return digit_images

digit_images = load_digit_images()

def draw_score(screen, score, digit_images):
    score_str = str(score)
    digit_height = digit_images[0].get_height() * 2  # Scale factor
    digit_width = digit_images[0].get_width() * 2
    total_width = sum(digit_width for digit in score_str)
    x_offset = (WIDTH - total_width) // 2

    for digit in score_str:
        digit_image = pygame.transform.scale(digit_images[int(digit)], (digit_width, digit_height))
        screen.blit(digit_image, (x_offset, 20))
        x_offset += digit_width

def check_score():
    global score
    # Ensuring we only count once per pipe pair
    for i in range(0, len(pipes), 2):
        pipe_top = pipes[i]
        pipe_bottom = pipes[i + 1]
        if not pipe_top.scored and pipe_top.rect.right < bird.rect.left:
            pipe_top.scored = pipe_bottom.scored = True
            score += 1
            bird.play_pass_pipe_sound()  # Play passing pipe sound

def main():
    global screen, avatar_birds, bird_select_sounds, bird_pass_pipe_sounds, clock, bird, selected_bird_index, difficulty, game_over, pipes, draw_score, popup_active, blink, last_blink_time, load_digit_images, mario_sound

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    avatar_birds = load_images(AVATAR_BIRDS, (50, 50))
    bird_select_sounds = load_sounds(BIRD_SELECT_SOUNDS)
    bird_pass_pipe_sounds = load_sounds(BIRD_PASS_PIPE_SOUNDS)
    mario_sound = pygame.mixer.Sound(MARIO_SOUND)
    selected_bird_index = 0  # default bird

    # Ensure no sound plays at the start except background music
    current_select_sound = None

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
                        selected_bird_index = (selected_bird_index - 1) % len(avatar_birds)
                        select_bird(selected_bird_index)
                    elif event.key == pygame.K_RIGHT:
                        selected_bird_index = (selected_bird_index + 1) % len(avatar_birds)
                        select_bird(selected_bird_index)
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
                    for i in range(len(avatar_birds)):
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
            draw_bird_selection_screen(screen, avatar_birds)
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
            if background_x <= -background_image.get_width():
                background_x = 0

            screen.blit(background_image, (background_x, 0))
            screen.blit(background_image, (background_x + background_image.get_width(), 0))

            all_sprites.update()
            all_sprites.draw(screen)
            generate_pipes(screen)
            check_score()
            draw_score(screen, score, digit_images)

            if pygame.sprite.spritecollideany(bird, pipes_group) or pygame.sprite.spritecollideany(bird, balls_group):
                game_running = False
                game_over = True

            pygame.display.update()
        elif game_over:
            draw_game_over_screen(screen)

        pygame.display.flip()
        clock.tick(60)

class Mario(pygame.sprite.Sprite):
    def __init__(self, group, all_sprites, x, y):
        super().__init__(group, all_sprites)
        self.image = pygame.image.load(MARIO_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (94, 110))  # Adjust Mario's size
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.initial_y = y
        self.counter = 0
        self.top = self.rect.y - 250  # value to control how far Mario moves up
        self.y_change = -2
        self.timer = 0
        self.fireball_timer = 0
        self.fireball_interval = 1000  # Time in milliseconds between fireballs
        self.fireball_count = 0
        self.fireball_limit = 5  # Number of fireballs Mario will launch
        self.direction = -1

    def update(self):
        if self.timer <= 0:
            if self.rect.y <= self.top:
                self.y_change = 0
                self.timer = 90  # Time Mario stays at the top before going down
                self.fireball_timer = pygame.time.get_ticks()  # Start fireball timer
            self.rect.y += self.y_change
        else:
            self.timer -= 1
            current_time = pygame.time.get_ticks()
            if self.fireball_count < self.fireball_limit and current_time - self.fireball_timer >= self.fireball_interval:
                fireball = Fireball(self.rect.center, self.get_fireball_direction())
                all_sprites.add(fireball)
                balls_group.add(fireball)
                self.fireball_timer = current_time
                self.fireball_count += 1

            if self.timer <= 0:
                self.y_change = 2
                if self.rect.y >= self.initial_y:
                    self.kill()  # Remove Mario once he goes back into the pipe  << not working

    def get_fireball_direction(self):
        bird_center_x, bird_center_y = bird.rect.center
        mario_center_x, mario_center_y = self.rect.center
        direction_x = bird_center_x - mario_center_x
        direction_y = bird_center_y - mario_center_y
        magnitude = (direction_x**2 + direction_y**2)**0.5
        return direction_x / magnitude, direction_y / magnitude

class Fireball(pygame.sprite.Sprite):
    def __init__(self, initial_position, direction):
        super().__init__()
        self.image = pygame.image.load(BALL_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))  # Adjust Fireball size
        self.rect = self.image.get_rect(center=initial_position)
        self.speed = 5
        self.direction = direction

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.kill()
        if self.rect.colliderect(bird.rect):  # Check collision with bird
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {}))  # Post game over event
            self.kill()

def generate_pipes(screen):
    global mario_timer
    gap = DIFFICULTIES[difficulty]['gap']
    pipe_speed = DIFFICULTIES[difficulty]['pipe_speed']
    last_pipe = pipes[-1] if pipes else None

    if not pipes or (last_pipe and last_pipe.rect.right < WIDTH - 300):
        pipe_height = random.randint(100, 300)
        pipe_top = Pipe(PIPE_IMAGE_PATH, (WIDTH, pipe_height - 400), size=(80, 400), rotate=True)
        pipe_bottom = Pipe(PIPE_IMAGE_PATH, (WIDTH, pipe_height + gap), size=(80, 400))
        pipes.extend([pipe_top, pipe_bottom])
        pipes_group.add(pipe_top, pipe_bottom)

        if len(pipes) // 2 % 4 == 0:
            mario = Mario(mario_group, all_sprites, pipe_bottom.rect.centerx, pipe_bottom.rect.bottom)
            all_sprites.add(mario)
            mario_group.add(mario)
            mario_sound.set_volume(1.0)
            mario_sound.play()

    pipes_group.update()
    pipes_group.draw(screen)

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
