# global_vars.py

import pygame

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
        '../assets/birds/bird2_flap.png',
        '../assets/birds/bird2_flop.png'
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
THEGODFATHER_IMAGE_PATH = '../assets/birds/mario.png'
BALL_IMAGE_PATH = '../assets/birds/ball.png'
BACKGROUND_MUSIC_PATH = '../assets/sounds/background_music.mp3'
BACKGROUND_IMAGE_PATH = '../assets/background.png'
PIPE_IMAGE_PATH = '../assets/pipes/pipe.png'
DIGIT_IMAGES_PATH = '../assets/digits'
FLOOR_IMAGE_PATH = '../assets/floor.png'

AVATAR_SIZE = (45, 60)
BIRD_SIZE = (77, 107)

DIFFICULTIES = {
    'easy': {'gap': 260, 'pipe_speed': 2},
    'hard': {'gap': 195, 'pipe_speed': 3},
    'advanced': {'gap': 130, 'pipe_speed': 4}
}

# Global variables initialization
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
bird = None

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
thegodfather_group = pygame.sprite.Group()
balls_group = pygame.sprite.Group()

print("global_vars loaded successfully")




