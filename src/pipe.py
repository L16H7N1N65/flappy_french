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
    __init__(self, image_path, initial_position, size=None, rotate=False):
        Initializes a new instance of Pipe with an image loaded from a PNG file.
    
    update(self):
        Updates the state of the pipe sprite each frame, moving it horizontally and handling removal when off-screen.
    """

    def __init__(self, image_path, initial_position, size=None, rotate=False):
        """
        Initializes a new instance of Pipe with an image loaded from a PNG file.

        Args:
        image_path (str): Path to the PNG image file for the pipe sprite.
        initial_position (tuple): Initial position (x, y) of the pipe sprite's top-left corner on the screen.
        size (tuple, optional): Desired size (width, height) of the pipe sprite. If provided, the image will be scaled to this size.
        rotate (bool, optional): Whether to rotate the image by 180 degrees. Default is False.
        """
        super().__init__()  # Initialize the parent class (pygame.sprite.Sprite)
        image = pygame.image.load(image_path)  # Load the image from the specified path
        if size is not None:
            image = pygame.transform.scale(image, size)  # Scale the image if a size is specified
        if rotate:
            image = pygame.transform.rotate(image, 180)  # Rotate the image by 180 degrees if specified
        self.image = image  # Set the loaded image as the pipe sprite's image
        self.rect = self.image.get_rect(topleft=initial_position)  # Create a Rect based on the initial position
        self.speed = 2  # Horizontal speed at which the pipe moves
        self.scored = False  # Track if the pipe has been scored

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