import pygame
from font import draw_text

def draw_start_screen(screen, blink, WIDTH, HEIGHT):
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

    draw_text("Press SPACE to start", "medium", (255, 255, 255), WIDTH // 2, HEIGHT - 50, screen)