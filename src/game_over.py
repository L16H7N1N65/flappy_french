import pygame
import os
import webbrowser
from font import draw_text
from global_vars import config
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.fx.resize import resize

def draw_game_over_screen(screen, config):
    config.popup_active = True
    pygame.mixer.music.stop()  # Stop the music when the game is over
    screen.fill((112, 197, 206))
    draw_text("Game Over", config.font_large, (0, 0, 0), config.WIDTH // 2, config.HEIGHT // 8, screen)
    draw_text(f"Your Score: {config.score}", config.font_medium, (0, 0, 0), config.WIDTH // 2, config.HEIGHT // 6 + 30, screen)

    bird_type = config.bird.bird_type
    video_path = config.BIRD_VIDEOS.get(bird_type, None)

    frames = []
    link_button_rect = None  # Initialize link button rectangle

    if video_path and os.path.exists(video_path):
        try:
            clip = VideoFileClip(video_path)
            clip = resize(clip, width=320, height=240)  # Resize to a fixed size
            config.audio_clip = AudioFileClip(video_path)  # Extract audio

            # Extract video frames
            for frame in clip.iter_frames(fps=24):
                frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                frames.append(frame_surface)
            config.video_frames = frames  # Store the frames for display

            # Save audio to a temporary file
            temp_audio_path = "temp_audio.wav"
            config.audio_clip.write_audiofile(temp_audio_path)

            # Load and play the audio using Pygame mixer
            pygame.mixer.music.load(temp_audio_path)
            pygame.mixer.music.play()

        except Exception as e:
            print(f"Error: Could not load video for {bird_type} - {str(e)}")
    else:
        print(f"Error: No video found for bird type {bird_type}")

    # Draw video frame area with a black contour
    if frames:
        video_frame_width = 320
        video_frame_height = 240
        video_frame_x = (config.WIDTH * 1 // 6)  # Center horizontally in the first two-thirds of the screen
        video_frame_y = config.HEIGHT // 4 + 30  # Slightly lower position

        # Draw the black border around the video frame
        video_border_rect = pygame.Rect(video_frame_x - 5, video_frame_y - 5, video_frame_width + 10, video_frame_height + 10)
        pygame.draw.rect(screen, (0, 0, 0), video_border_rect, 5)

        # Draw the video frame itself
        screen.blit(frames[0], (video_frame_x, video_frame_y))

        # Position the link button below the video frame
        link_button_width = frames[0].get_width()
        link_button_height = 50
        link_button_x = video_frame_x + (video_frame_width - link_button_width) // 2
        link_button_y = video_frame_y + video_frame_height + 10
        link_button_rect = pygame.Rect(link_button_x, link_button_y, link_button_width, link_button_height)
        pygame.draw.rect(screen, (0, 0, 255), link_button_rect)
        draw_text("Click for more...", config.font_medium, (255, 255, 255), link_button_rect.centerx, link_button_rect.centery, screen)

    # Buttons on the right side
    button_width = config.WIDTH // 5
    button_height = 50
    button_spacing = 20
    start_x = config.WIDTH * 2 // 3
    start_y = config.HEIGHT // 3

    buttons = [
        ("About me", start_x),
        ("Play Again", start_x),
        ("Stop Game", start_x),
        ("Élections 24", start_x)
    ]

    button_rects = []
    for idx, (text, button_x) in enumerate(buttons):
        button_rect = pygame.Rect(button_x, start_y + idx * (button_height + button_spacing), button_width, button_height)
        pygame.draw.rect(screen, (255, 0, 0), button_rect)
        draw_text(text, config.font_medium, (255, 255, 255), button_rect.centerx, button_rect.centery, screen)
        button_rects.append((text, button_rect))

    pygame.display.update()
    print("Game over screen drawn with buttons:", buttons)
    return button_rects, link_button_rect if frames else None

def play_video_on_screen(screen, frames, pos=(50, 150)):
    for frame in frames:
        screen.blit(frame, pos)
        pygame.display.update()
        pygame.time.wait(int(1000 / 24))  # Adjust this to match the frame rate of the video

print("game_over.py loaded successfully")








