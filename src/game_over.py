#game_over.py

import pygame
from font import draw_text

def draw_game_over_screen(screen, score, font_large, font_medium, WIDTH, HEIGHT):
    global popup_active
    popup_active = True
    pygame.mixer.music.stop()  # Stop the music when the game is over
    screen.fill((112, 197, 206))
    draw_text("Game Over", font_large, (0, 0, 0), WIDTH // 2, HEIGHT // 4, screen)
    draw_text(f"Your Score: {score}", font_medium, (0, 0, 0), WIDTH // 2, HEIGHT // 2, screen)

    button_width = WIDTH // 5  # Smaller button width to fit all buttons on screen
    button_height = 50
    button_spacing = 20
    start_x = (WIDTH - (button_width * 4 + button_spacing * 3)) // 2
    start_y = HEIGHT * 3 // 4

    buttons = [
        ("About me", start_x),
        ("Play Again", start_x + button_width + button_spacing),
        ("Stop Game", start_x + 2 * (button_width + button_spacing)),
        ("Visit Website", start_x + 3 * (button_width + button_spacing))
    ]

    for text, button_x in buttons:
        button_rect = pygame.Rect(button_x, start_y, button_width, button_height)
        pygame.draw.rect(screen, (255, 0, 0), button_rect)
        draw_text(text, font_medium, (255, 255, 255), button_rect.centerx, button_rect.centery, screen)

    pygame.display.update()
    print("Game over screen drawn with buttons:", buttons)




