import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pixel Adventure")

# Colors
WHITE = (255, 255, 255)

# Load character sprite from local path
character_path = "/assets/images/character.png"
character = pygame.image.load(character_path).convert_alpha()

# Scaling factor for character relative to screen size
character_scale_factor = 0.1

def scale_character():
    global character, character_rect
    new_size = (int(WIDTH * character_scale_factor), int(HEIGHT * character_scale_factor))
    character = pygame.transform.scale(character, new_size)
    character_rect = character.get_rect()
    character_rect.topleft = (50, 50)

scale_character()

# Movement variables
move_left = False
move_right = False
gravity = 0.0025
base_speed = 0.75
character_speed = base_speed
sprint_multiplier = 2
character_velocity_y = 0
jump_height = -0.75
jump_count = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            scale_character()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                move_left = True
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                move_right = True
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                character_speed = base_speed * sprint_multiplier
            if event.key == pygame.K_SPACE:
                if jump_count < 2:
                    character_velocity_y = jump_height
                    jump_count += 1
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                move_left = False
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                move_right = False
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                character_speed = base_speed

    # Apply gravity
    character_velocity_y += gravity
    character_rect.y += character_velocity_y

    # Prevent falling through the floor
    if character_rect.bottom >= HEIGHT:
        character_rect.bottom = HEIGHT
        character_velocity_y = 0
        jump_count = 0

    # Move character
    if move_left and move_right:
        pass
    elif move_left and character_rect.left > 0:
        character_rect.x -= character_speed
    elif move_right and character_rect.right < WIDTH:
        character_rect.x += character_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the character
    screen.blit(character, character_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()