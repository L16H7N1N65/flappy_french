## pipe.py

import pygame

class Pipe(pygame.sprite.Sprite):
    """
    Pipe class represents a moving obstacle in the game.

    Attributes:
    image (Surface): Image of the pipe sprite.
    rect (Rect): Rectangle that defines the position and size of the pipe sprite on the screen.
    speed (int): Horizontal speed at which the pipe moves.
    
    Methods:
    __init__(self, image, initial_position):
        Initializes a new instance of Pipe with initial attributes.
    
    update(self):
        Updates the state of the pipe sprite each frame, moving it horizontally and handling removal when off-screen.
    """

    def __init__(self, image, initial_position):
        """
        Initializes a new instance of Pipe.

        Args:
        image (Surface): Image of the pipe sprite.
        initial_position (tuple): Initial position (x, y) of the pipe sprite's top-left corner on the screen.
        """
        super().__init__()  # Initialize the parent class (pygame.sprite.Sprite)
        self.image = image  # Set the image of the pipe sprite
        self.rect = self.image.get_rect(topleft=initial_position)  # Create a Rect based on the initial position
        self.speed = 2  # Horizontal speed at which the pipe moves

    def update(self):
        """
        Updates the state of the pipe sprite each frame.

        This method moves the pipe horizontally to the left and removes it if it moves off-screen.
        """
        self.rect.x -= self.speed  # Move the pipe sprite horizontally to the left

        # Check if the right edge of the pipe sprite has moved completely off the left side of the screen
        if self.rect.right < 0:
            self.kill()  # Remove the pipe sprite from all sprite groups it belongs to

    """
    Note to myself:
    
    Replace generated pipes by png loaded in assets folder
    
    """