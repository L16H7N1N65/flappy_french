

# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "numpy",    
#   "pygame-ce",
#   "imageio",
#   "imageio-ffmpeg",
#   "moviepy",
#   "pygbag",
#   "certifi",
#   "charset-normalizer",
#   "decorator",
#   "idna",
#   "opencv-python",
#   "opencv-python-headless",
#   "Pillow",
#   "proglog",
#   "requests",
#   "tqdm",
#   "urllib3"
# ]
# ///

import pygame
import asyncio
import sys

import os
import subprocess

from src.my_game import main as game_main

async def async_main():
    await game_main()

def is_web_runtime():
    return 'WEB_RUNTIME' in os.environ

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError:
        pass

def main():
    if not is_web_runtime():
        install_dependencies()
    else:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
        except subprocess.CalledProcessError:
            pass
    
    asyncio.run(async_main())

if __name__ == "__main__":
    main()


