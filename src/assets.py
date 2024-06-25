from load_images import load_images, load_sounds
from global_vars import AVATAR_BIRDS, BIRD_SELECT_SOUNDS, BIRD_PASS_PIPE_SOUNDS

def load_assets():
    avatar_birds = load_images(AVATAR_BIRDS, (50, 50))
    bird_select_sounds = load_sounds(BIRD_SELECT_SOUNDS)
    bird_pass_pipe_sounds = load_sounds(BIRD_PASS_PIPE_SOUNDS)
    return avatar_birds, bird_select_sounds, bird_pass_pipe_sounds
