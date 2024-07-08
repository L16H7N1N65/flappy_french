# my_game.py

import pygame
import sys
import webbrowser
import asyncio
from src.select_bird import select_bird, draw_bird_selection_screen
from src.pipe import Pipe, generate_pipes, check_score, set_difficulty
from src.assets import load_images, load_sounds, load_digit_images
from src.init import initialize
from src.global_vars import config
from src.draw_start_screen import draw_start_screen
from src.game_over import draw_game_over_screen, play_video_on_screen
from src.font import draw_text
from src.thegodfather import TheGodfather
from src.start_game import start_game
from src.floor import Floor

digit_images = load_digit_images(config.DIGIT_IMAGES_PATH)
score = check_score

def draw_score(screen, score, digit_images):
    score_str = str(score)
    digit_height = digit_images[0].get_height() * 2
    digit_width = digit_images[0].get_width() * 2
    total_width = sum(digit_width for digit in score_str)
    x_offset = (config.WIDTH - total_width) // 2

    for digit in score_str:
        digit_image = pygame.transform.scale(digit_images[int(digit)], (digit_width, digit_height))
        screen.blit(digit_image, (x_offset, 20))
        x_offset += digit_width

async def main():
    global screen, clock, bird, game_over, button_rects, link_button_rect
    screen, clock = initialize()

    config.bird_select_sounds = load_sounds(config.BIRD_SELECT_SOUNDS)
    config.bird_pass_pipe_sounds = load_sounds(config.BIRD_PASS_PIPE_SOUNDS)
    config.THEGODFATHER_SOUND = pygame.mixer.Sound(config.THEGODFATHER_SOUND)
    current_select_sound = None

    selected_bird_index = 0

    avatar_birds = load_images(config.AVATAR_BIRDS, (50, 50))
    background_image = pygame.image.load(config.BACKGROUND_IMAGE_PATH).convert()
    background_image = pygame.transform.scale(background_image, (config.WIDTH, config.HEIGHT))

    # Initialize and configure floor
    floor = Floor(config.FLOOR_IMAGE_PATH, config.WIDTH, config.HEIGHT)
    config.floor = floor

    bird_number = None
    url = config.bird_links.get(bird_number)

    start_screen = True
    bird_selection_screen = False
    difficulty_screen = False
    game_running = False
    blink = False
    bird = None
    game_over = False
    button_rects = []

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
                    if event.key == pygame.K_LEFT:
                        selected_bird_index = (selected_bird_index - 1) % len(avatar_birds)
                        bird = select_bird(selected_bird_index)
                    elif event.key == pygame.K_RIGHT:
                        selected_bird_index = (selected_bird_index + 1) % len(avatar_birds)
                        bird = select_bird(selected_bird_index)
                    elif event.key == pygame.K_RETURN:
                        if bird is not None:
                            bird_selection_screen = False
                            difficulty_screen = True
                        else:
                            print("Error: Bird is not initialized!")
                elif difficulty_screen:
                    if bird is None:
                        print("Error: Bird is not initialized!")
                        continue
                    if event.key == pygame.K_UP:
                        set_difficulty('easy')
                        difficulty_screen = False
                        game_running = True
                    elif event.key == pygame.K_DOWN:
                        set_difficulty('advanced')
                        difficulty_screen = False
                        game_running = True
                    elif event.key == pygame.K_RIGHT:
                        set_difficulty('hard')
                        difficulty_screen = False
                        game_running = True
                elif game_running:
                    if event.key == pygame.K_SPACE:
                        bird.jump()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_screen:
                    start_screen = False
                    bird_selection_screen = True
                elif bird_selection_screen:
                    button_width, button_height = 120, 80
                    for i in range(len(avatar_birds)):
                        row = i // 4
                        col = i % 4
                        button_x = (config.WIDTH // 2 - (button_width * 4 + 30) // 2) + col * (button_width + 10)
                        button_y = config.HEIGHT // 2 + row * (button_height + 10)
                        if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
                            selected_bird_index = i
                            bird = select_bird(selected_bird_index)
                            print(f"Bird selected at index {selected_bird_index}: {bird}")
                    start_img_rect = pygame.Rect((config.WIDTH // 2 - button_width // 2, config.HEIGHT - 100, button_width, button_height))
                    if start_img_rect.collidepoint(event.pos):
                        if bird is not None:
                            if config.current_select_sound:
                                config.current_select_sound.stop()
                            start_sound = pygame.mixer.Sound(config.START_SOUND_PATH)
                            start_sound.play()
                            bird_selection_screen = False
                            difficulty_screen = True
                        else:
                            print("Start button clicked, but bird is not initialized.")
                elif difficulty_screen:
                    easy_rect = pygame.Rect(config.WIDTH // 4, config.HEIGHT // 2 - 30, config.WIDTH // 2, 60)
                    hard_rect = pygame.Rect(config.WIDTH // 4, config.HEIGHT // 2 + 40, config.WIDTH // 2, 60)
                    advanced_rect = pygame.Rect(config.WIDTH // 4, config.HEIGHT // 2 + 110, config.WIDTH // 2, 60)
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
                elif game_over and config.popup_active:
                    for text, button_rect in button_rects:
                        if button_rect.collidepoint(event.pos):
                            print(f"Button '{text}' clicked.")
                            if text == "About me":
                                webbrowser.open('https://shorturl.at/rjqOQ')
                            elif text == "Play Again":
                                # Reset game state and start a new game
                                config.popup_active = False
                                game_over = False
                                game_running = True
                                start_game()  # Restart the game logic
                            elif text == "Stop Game":
                                pygame.quit()
                                sys.exit()
                            elif text == "Élections 24":
                                webbrowser.open('https://shorturl.at/3lP1j')
                            elif text == "Play Video":
                                config.video_playing = True
                            elif text == "Pause":
                                config.video_playing = False
                            elif text == "Link":
                                webbrowser.open(url)

        if start_screen:
            current_time = pygame.time.get_ticks()
            if current_time - config.last_blink_time >= config.blink_speed:
                blink = not blink
                config.last_blink_time = current_time
            draw_start_screen(screen, blink)
        elif bird_selection_screen:
            start_img_rect = draw_bird_selection_screen(screen, avatar_birds)
        elif difficulty_screen:
            screen.fill(config.BACKGROUND_COLOR)
            draw_text("Select Difficulty", config.font_large, (0, 0, 0), config.WIDTH // 2, config.HEIGHT // 4, screen)
            easy_rect = pygame.draw.rect(screen, (255, 255, 255), (config.WIDTH // 4, config.HEIGHT // 2 - 30, config.WIDTH // 2, 60))
            hard_rect = pygame.draw.rect(screen, (255, 255, 255), (config.WIDTH // 4, config.HEIGHT // 2 + 40, config.WIDTH // 2, 60))
            advanced_rect = pygame.draw.rect(screen, (255, 255, 255), (config.WIDTH // 4, config.HEIGHT // 2 + 110, config.WIDTH // 2, 60))
            draw_text("Easy", config.font_medium, (0, 0, 0), easy_rect.centerx, easy_rect.centery, screen)
            draw_text("Hard", config.font_medium, (0, 0, 0), hard_rect.centerx, hard_rect.centery, screen)
            draw_text("Advanced", config.font_medium, (0, 0, 0), advanced_rect.centerx, advanced_rect.centery, screen)
        elif game_running:
            if bird is None:
                print("Error: Bird is not initialized!")
                continue
            screen.blit(background_image, (0, 0))
            config.pipes_group.update()
            config.pipes_group.draw(screen)
            config.votes_group.update()
            config.votes_group.draw(screen)
            floor.update()
            floor.draw(screen)
            config.all_sprites.update()
            config.all_sprites.draw(screen)
            generate_pipes()
            draw_score(screen, config.score, digit_images)
            for i in range(0, len(config.pipes), 2):
                check_score(config.pipes[i], config.pipes[i + 1], bird)
            if pygame.sprite.spritecollideany(bird, config.pipes_group) or pygame.sprite.spritecollideany(bird, config.balls_group):
                game_running = False
                game_over = True

            pygame.display.update()
        if game_over:
            button_rects, link_button_rect = draw_game_over_screen(screen, config)
            if config.video_frames and config.video_playing:
                play_video_on_screen(screen, config.video_frames, (config.WIDTH // 2 - 160, config.HEIGHT // 4 + 30))

        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)
    print("game loaded successfully")

if __name__ == "__main__":
    asyncio.run(main())































"""
#### Note my self

## restrain birds to a fixed sized                                       <<<<<<<<<<<< done
## Pipes logic isnt working -- to be fixed !                             <<<<<<<<<<<< done
## Create a video before after screen start                              <<<<<<<<<<<< done
## modify bird mov from mouse to keyup and keydown                       <<<<<<<<<<<< done however replaced with space bar to fly
## redefine pop up when the game is lost                                 <<<<<<<<<<<< reverted to basics, it works but needs style
## Birds shall be centered on start 4 x 4                                <<<<<<<<<<<< done
## Birds are still randomnly chosen when game starts

## sounds when choosing the bird                                          <<<<<<<<<<<< done
## sounds when game is lost                                               <<<<<<<<<<<< pending
## sounds when game is won                                                <<<<<<<<<<<< pending
## sounds during game                                                     <<<<<<<<<<<< done
## Add a score board and load the assests                                 <<<<<<<<<<<< done

## background modify                                                      <<<<<<<<<<<< done
## floor must be included                                                 <<<<<<<<<<<< done

## Generate sounds for flap                                               <<<<<<<<<<<< done
## Create sound when the game is lost                                     <<<<<<<<<<<< pending
## Create background                                                      <<<<<<<<<<<< done

## Create a score board                                                   <<<<<<<<<<<< pending
## Create a pause button                                                  <<<<<<<<<<<< pending
## Create a restart button                                                <<<<<<<<<<<< done
## Create a stop button                                                   <<<<<<<<<<<< pending
## Create a start button                                                  <<<<<<<<<<<< done

## Modify pdf by about me                                                 <<<<<<<<<<<< pending

"""
