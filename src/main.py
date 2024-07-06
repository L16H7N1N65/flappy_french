"""
    Flappy French
    Copyright (C) 2024  L16H7N1N65

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    You can contact me at linda.meghouche@gmail.com
"""

import pygame
import sys
import asyncio
from game import main as game_main

async def async_main():
    await game_main()

if __name__ == "__main__":
    asyncio.run(async_main())
