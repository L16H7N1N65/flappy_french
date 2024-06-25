import pygame
from global_vars import font_large, font_medium, font_small

def draw_text(text, font, color, x, y, screen):
    if font == "large":
        font_to_use = font_large
    elif font == "medium":
        font_to_use = font_medium
    elif font == "small":
        font_to_use = font_small
    else:
        raise ValueError(f"Invalid font type '{font}'. Expected 'large', 'medium', or 'small'.")

    text_surface = font_to_use.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
