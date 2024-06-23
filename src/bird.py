## bird.py

import pygame

class Bird(pygame.sprite.Sprite):
    """
    Bird class represents the player-controlled sprite in the game.

    Attributes:
    images (list): A list of images representing different frames of the bird's animation.
    image (Surface): Current image of the bird sprite.
    rect (Rect): Rectangle that defines the position and size of the bird sprite on the screen.
    velocity (float): Vertical velocity of the bird sprite.
    gravity (float): Acceleration due to gravity applied to the bird sprite each frame.
    jump_velocity (float): Vertical velocity applied to the bird sprite when it jumps upwards.
    is_jumping (bool): Flag indicating whether the bird is currently jumping.

    Methods:
    __init__(self, images, initial_position):
        Initializes a new instance of Bird with initial attributes.
    
    update(self):
        Updates the state of the bird sprite each frame, including gravity and boundary checks.
    
    jump(self):
        Initiates a jump action for the bird sprite.
    
    animate(self):
        Placeholder method for animating the bird sprite.
    """

    def __init__(self, images, initial_position):
        """
        Initializes a new instance of Bird.

        Args:
        images (list): A list of Surface objects representing different frames of the bird's animation.
        initial_position (tuple): Initial position (x, y) of the bird sprite's center on the screen.
        """
        super().__init__()
        self.images = images  # Store the list of bird images
        self.image = self.images[0]  # Set the initial image to the first image in the list
        self.rect = self.image.get_rect(center=initial_position)  # Create a Rect based on the initial position
        self.velocity = 0  # Initialize vertical velocity
        self.gravity = 0.9  # Acceleration due to gravity
        self.jump_velocity = -10  # Vertical velocity when jumping upwards
        self.is_jumping = False  # Flag indicating whether the bird is jumping

    def update(self):
        """
        Updates the state of the bird sprite each frame.

        This method handles gravity, movement, and animation of the bird sprite.
        """
        self.velocity += self.gravity  # Apply gravity to the vertical velocity
        self.rect.y += self.velocity  # Update the bird's position based on its velocity

        # Boundary checks to prevent the bird from going off-screen
        if self.rect.top <= 0:
            self.rect.top = 0  # Keep the bird at the top edge of the screen
            self.velocity = 0  # Stop vertical movement
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600  # Keep the bird at the bottom edge of the screen
            self.velocity = 0  # Stop vertical movement

        if self.is_jumping:
            self.animate()  # If the bird is jumping, call the animate method

    def jump(self):
        """
        Initiates a jump action for the bird sprite.
        """
        self.velocity = self.jump_velocity  # Set the bird's velocity to jump upwards
        self.is_jumping = True  # Set the jumping flag to True

    def animate(self):
        """
        Placeholder method for animating the bird sprite.

        This method will handle the animation of the bird, switching between different images
        in self.images to create the appearance of movement.
        """
        pass  # Currently not implemented; will handle animation logic in the future

        """
        Notes to myself :
        
        later on create 2 images to animate the bird
        
        """

