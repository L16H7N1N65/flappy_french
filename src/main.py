## main.py

import pygame
import sys
from game import main

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((800, 600))  ## updated here intend is initialize display bf loading img
    main()
    pygame.quit()

