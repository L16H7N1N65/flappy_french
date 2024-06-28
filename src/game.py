import pygame
import sys
import webbrowser
from select_bird import select_bird, draw_bird_selection_screen
from pipe import Pipe, generate_pipes, check_score
from assets import load_images, load_sounds, load_digit_images
from init import initialize
from global_vars import *
from draw_start_screen import draw_start_screen
from game_over import draw_game_over_screen
from font import draw_text
from thegodfather import TheGodfather
from start_game import start_game, set_difficulty
from bird import Bird



digit_images = load_digit_images(DIGIT_IMAGES_PATH)

def draw_score(screen, score, digit_images):
    score_str = str(score)
    digit_height = digit_images[0].get_height() * 2
    digit_width = digit_images[0].get_width() * 2
    total_width = sum(digit_width for digit in score_str)
    x_offset = (WIDTH - total_width) // 2

    for digit in score_str:
        digit_image = pygame.transform.scale(digit_images[int(digit)], (digit_width, digit_height))
        screen.blit(digit_image, (x_offset, 20))
        x_offset += digit_width

def main():
    global screen, avatar_birds, bird_select_sounds, Bird, bird_pass_pipe_sounds, clock, bird, selected_bird_index, difficulty, game_over, pipes, draw_score, popup_active, blink, last_blink_time, mario_sound, current_select_sound, Pipe, check_score, TheGodfather
    # Initialize pygame
    screen, clock = initialize()
    
    # Load sounds
    bird_select_sounds = load_sounds(BIRD_SELECT_SOUNDS)
    bird_pass_pipe_sounds = load_sounds(BIRD_PASS_PIPE_SOUNDS)
    mario_sound = pygame.mixer.Sound(MARIO_SOUND)
    current_select_sound = None
    
    # Default bird
    selected_bird_index = 0
    
    # Load images
    avatar_birds = load_images(AVATAR_BIRDS, (50, 50))
    background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    
    # Load floor image
    floor_image = pygame.image.load(FLOOR_IMAGE_PATH).convert_alpha()
    floor_height = floor_image.get_height() // 10  
    floor_image = pygame.transform.scale(floor_image, (WIDTH, floor_height))
    floor_x = 0
    
    # Initialize groups
    start_screen = True
    bird_selection_screen = False
    difficulty_screen = False
    game_running = False
    blink = False
    bird = None  # Ensure bird is defined globally
    
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
                    print(f"Error 78 :{bird}")
                    if event.key == pygame.K_LEFT:
                        selected_bird_index = (selected_bird_index - 1) % len(avatar_birds)
                        bird = select_bird(selected_bird_index, bird_select_sounds, bird_pass_pipe_sounds, ANIMATED_BIRDS, AVATAR_BIRDS)
                        print(f"Error 82 :{bird}")
                    elif event.key == pygame.K_RIGHT:
                        selected_bird_index = (selected_bird_index + 1) % len(avatar_birds)
                        bird = select_bird(selected_bird_index, bird_select_sounds, bird_pass_pipe_sounds, ANIMATED_BIRDS, AVATAR_BIRDS)
                    elif event.key == pygame.K_RETURN:
                        if bird is not None:
                            bird_selection_screen = False
                            difficulty_screen = True
                elif difficulty_screen:
                    if event.key == pygame.K_UP:
                        set_difficulty('easy')  
                    elif event.key == pygame.K_DOWN:
                        set_difficulty('advanced')
                    elif event.key == pygame.K_RIGHT:
                        set_difficulty('hard')
                    difficulty_screen = False
                    game_running = True
                    print(f"Error 99 :{bird}")
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
                    button_width, button_height = 120, 80
                    for i in range(len(avatar_birds)):
                        row = i // 4
                        col = i % 4
                        button_x = (WIDTH // 2 - (button_width * 4 + 30) // 2) + col * (button_width + 10)
                        button_y = HEIGHT // 2 + row * (button_height + 10)
                        if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
                            selected_bird_index = i
                            select_bird(selected_bird_index, bird_select_sounds, bird_pass_pipe_sounds, ANIMATED_BIRDS, AVATAR_BIRDS)
                    start_img_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT - 100, button_width, button_height))
                    if start_img_rect.collidepoint(event.pos):
                        if bird is not None:
                            bird_selection_screen = False
                            difficulty_screen = True
                        else:
                            print("Start button clicked, but bird is not initialized.")
                elif difficulty_screen:
                    x, y = event.pos
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
            start_img_rect = draw_bird_selection_screen(screen, avatar_birds)
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
            if bird is None:
                print("Error: Bird is not initialized!")
                continue
            screen.blit(background_image, (0, 0))
            pipes_group.update()
            pipes_group.draw(screen)
            floor_x -= 2
            if floor_x <= -WIDTH:
                floor_x = 0
            screen.blit(floor_image, (floor_x, HEIGHT - floor_height))
            screen.blit(floor_image, (floor_x + WIDTH, HEIGHT - floor_height))
            all_sprites.update()
            all_sprites.draw(screen)
            generate_pipes()
            draw_score(screen, score, digit_images)
            if pygame.sprite.spritecollideany(bird, pipes_group) or pygame.sprite.spritecollideany(bird, balls_group):
                game_running = False
                game_over = True
            pygame.display.update()
        elif game_over:
            draw_game_over_screen(screen)
        pygame.display.flip()
        clock.tick(60)

print("game loaded successfully")

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
