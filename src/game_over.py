import pygame
from font import draw_text

def draw_game_over_screen(screen, score, font_large, font_medium, WIDTH, HEIGHT):
    global popup_active
    popup_active = True
    pygame.mixer.music.stop()  # Stop the music when the game is over
    screen.fill((112, 197, 206))
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

