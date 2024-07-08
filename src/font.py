from src.global_vars import config

def draw_text(text, font, color, x, y, surface):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

print("font loaded successfully")


