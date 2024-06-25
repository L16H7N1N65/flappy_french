## main.py
import pygame
from game import main

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((800, 600))  # Dummy window 
    main()
    pygame.quit()



print("main.py executed successfully")
