"""
SECRETLY YOU - Main Entry Point
A Stardew Valley-style visual novel game
"""

import pygame
import sys
from engine.game import Game

def main():
    pygame.init()
    pygame.mixer.init()
    
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    FPS = 60
    TITLE = "Secretly You"

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    game = Game(screen, clock, FPS)
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
