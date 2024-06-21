import pygame
from settings import *


def handle_input(player, running):
    """
    Handles user input for controlling the player and game state.

    Parameters:
        player (Player): The player object to control.
        running (bool): The current running state of the game.

    Returns:
        bool: Updated running state of the game.
    """
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Reset horizontal movement speed
    player.speed_x = 0

    # Move left: If left arrow key or 'A' key is pressed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.speed_x = -PLAYER_SPEED

    # Move right: If right arrow key or 'D' key is pressed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.speed_x = PLAYER_SPEED

    # Sprint: If left shift key is pressed
    if keys[pygame.K_LSHIFT]:
        player.speed_x *= SPRINT_MULTIPLIER

    # Jump: If spacebar is pressed
    if keys[pygame.K_SPACE]:
        player.jump()

    # Drop through platforms: If down arrow key or 'S' key is pressed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.drop()

    # Exit the game: If escape key is pressed
    if keys[pygame.K_ESCAPE]:
        running = False

    return running