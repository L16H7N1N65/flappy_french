import pygame
import sys
from game import initialize_game

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (112, 197, 206)  # light blue

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Clock for controlling FPS
clock = pygame.time.Clock()

def main():
    initialize_game(screen, clock)

    # Main game loop
    while True:
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

pygame.quit()
