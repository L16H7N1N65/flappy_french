import pygame
import sys
import asyncio
from game import main as game_main

async def async_main():
    await game_main()

if __name__ == "__main__":
    asyncio.run(async_main())
