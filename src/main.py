import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Adventure")

# Colors
WHITE = (255, 255, 255)

# Load character sprite
character_path = os.path.join(os.path.dirname(__file__), '../assets/images/character.png')
character = pygame.image.load(character_path)
character = pygame.transform.scale(character, (50, 50))  # Resize character sprite if necessary
character_rect = character.get_rect()
character_rect.topleft = (50, 50)

# Movement variables
move_left = False
move_right = False
gravity = 0.5
character_speed = 2.5  # Half the speed
character_velocity_y = 0
jump_height = -20  # Twice the jump height
jump_count = 0  # To keep track of the number of jumps

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_SPACE:
                if jump_count < 2:  # Allow double jump
                    character_velocity_y = jump_height
                    jump_count += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    # Apply gravity
    character_velocity_y += gravity
    character_rect.y += character_velocity_y

    # Prevent falling through the floor
    if character_rect.bottom >= HEIGHT:
        character_rect.bottom = HEIGHT
        character_velocity_y = 0
        jump_count = 0  # Reset jump count when character lands

    # Move character
    if move_left and character_rect.left > 0:
        character_rect.x -= character_speed
    if move_right and character_rect.right < WIDTH:
        character_rect.x += character_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the character
    screen.blit(character, character_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()
