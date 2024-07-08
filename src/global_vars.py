class Config:
    def __init__(self):
        import pygame
        pygame.init()
        pygame.mixer.init()
        self.video_playing = False
        self.video_pause = False
        self.WIDTH, self.HEIGHT = 800, 600
        self.BACKGROUND_COLOR = (112, 197, 206)

        self.LOGO_IMAGE_PATH = 'assets/logo.png'
        self.BACKGROUND_INITIAL_PATH = 'assets/bg_initial.png'
        self.INITIAL_START_IMAGE_PATH = 'assets/initial_start.png'

        self.AVATAR_BIRDS = [
            'assets/birds/bird1.png',
            'assets/birds/bird2.png',
            'assets/birds/bird3.png',
            'assets/birds/bird4.png',
            'assets/birds/bird5.png',
            'assets/birds/bird6.png',
            'assets/birds/bird7.png',
            'assets/birds/bird8.png'
        ]

        self.bird_links = {
            'bird1': [
                'https://parti-renaissance.fr',
            ],
            'bird2': [
                'https://mlafrance.fr/programme',
            ],
            'bird3': [
                'https://melenchon2022.fr/programme',
            ],
            'bird4': [
                'https://programme.ericzemmour.fr',
            ],
        }

        self.ANIMATED_BIRDS = {
            'bird1': [
                'assets/birds/bird1_flap.png',
                'assets/birds/bird1_flop.png'
            ],
            'bird2': [
                'assets/birds/bird2_flap.png',
                'assets/birds/bird2_flop.png'
            ],
            'bird3': [
                'assets/birds/bird3_flap.png',
                'assets/birds/bird3_flop.png'
            ],
            'bird4': [
                'assets/birds/bird4_flap.png',
                'assets/birds/bird4_flop.png'
            ],
        }

        self.BIRD_SELECT_SOUNDS = [
            'assets/sounds/select1.ogg',
            'assets/sounds/select2.ogg',
            'assets/sounds/select3.ogg',
            'assets/sounds/select4.ogg',
            'assets/sounds/select5.ogg',
            'assets/sounds/select6.ogg',
            'assets/sounds/select7.ogg',
            'assets/sounds/select8.ogg'
        ]

        self.BIRD_PASS_PIPE_SOUNDS = [
            'assets/sounds/pass_pipe1.ogg',
            'assets/sounds/pass_pipe2.ogg',
            'assets/sounds/pass_pipe3.ogg',
            'assets/sounds/pass_pipe4.ogg',
            'assets/sounds/pass_pipe5.ogg',
            'assets/sounds/pass_pipe6.ogg',
            'assets/sounds/pass_pipe7.ogg',
            'assets/sounds/pass_pipe8.ogg'
        ]

        self.VOTE_PATH = 'assets/vote.png'
        self.THEGODFATHER_SOUND = 'assets/sounds/thegodfather.ogg'
        self.THEGODFATHER_IMAGE_PATH = 'assets/birds/thegodfather.png'
        self.BALL_IMAGE_PATH = 'assets/birds/ball.png'
        self.BACKGROUND_MUSIC_PATH = 'assets/sounds/background_music.ogg'
        self.BACKGROUND_IMAGE_PATH = 'assets/background.png'

        self.PIPE_IMAGE_PATH = 'assets/pipes/pipe.png'
        self.DIGIT_IMAGES_PATH = 'assets/digits'
        self.FLOOR_IMAGE_PATH = 'assets/floor.png'
        self.START_IMAGE_PATH = 'assets/start.png'
        self.START_SOUND_PATH = 'assets/sounds/start.ogg'

        self.BIRD_VIDEOS = {
            'bird1': 'assets/videos/bird1.webm',
            'bird2': 'assets/videos/bird2.webm',
            'bird3': 'assets/videos/bird3.webm',
            'bird4': 'assets/videos/bird4.webm'
        }

        self.AVATAR_SIZE = (45, 60)
        self.BIRD_SIZE = (77, 107)

        self.DIFFICULTIES = {
            'easy': {'gap': 260, 'pipe_speed': 2},
            'hard': {'gap': 195, 'pipe_speed': 3},
            'advanced': {'gap': 130, 'pipe_speed': 4}
        }

        # Global var initialization
        self.avatar_birds = []
        self.bird_select_sounds = []
        self.bird_pass_pipe_sounds = []
        self.thegodfather = []
        self.bird_image = None
        self.selected_bird_index = 0
        self.difficulty = ''
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.popup_active = False
        self.current_select_sound = None
        self.bird = None
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Blinking related var
        self.last_blink_time = 0
        self.blink_speed = 500

        self.font_large = pygame.font.SysFont('Arial', 50)
        self.font_medium = pygame.font.SysFont('Arial', 30)
        self.font_small = pygame.font.SysFont('Arial', 15)

        # Sprites group
        self.all_sprites = pygame.sprite.Group()
        self.pipes_group = pygame.sprite.Group()
        self.votes_group = pygame.sprite.Group()
        self.balls_group = pygame.sprite.Group()
        self.thegodfather_group = pygame.sprite.Group()

config = Config()










