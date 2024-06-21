import os
import pygame

# Initialize pygame to use display functions
pygame.init()

# Get the display information
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

BG_COLOR = (50, 50, 50)
TILE_SIZE = 50

# Player settings
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
PLAYER_COLOR = (255, 0, 0)
PLAYER_SPEED = 5
GRAVITY = 0.5
JUMP_HEIGHT = 12.5
SPRINT_MULTIPLIER = 2

# Local path of the character image
LOCAL_CHARACTER_IMAGE_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'character.png')
