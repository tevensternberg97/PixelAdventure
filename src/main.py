import pygame
import sys
import requests
from io import BytesIO

# Game settings
REFERENCE_WIDTH = 800  # Reference width for consistent speed
REFERENCE_HEIGHT = 600  # Reference height for consistent speed
CHARACTER_SCALE = 0.05  # Character size as a fraction of screen size
BASE_SPEED_SCALE = 0.002  # Base speed as a fraction of reference width
SPRINT_MULTIPLIER = 2  # Speed multiplier when sprinting
GRAVITY_SCALE = 0.00008  # Gravity as a fraction of reference height
JUMP_HEIGHT_MULTIPLIER = 0.042  # Jump height as a multiple of character's height

# Character size settings
CHARACTER_WIDTH_PIXELS = 100  # Character width in pixels
CHARACTER_HEIGHT_PIXELS = 150  # Character height in pixels

# URL of the character image
CHARACTER_IMAGE_URL = "https://github.com/tevensternberg97/PixelAdventure/raw/18926c7c94fb9040e4542daf6ead5d5956cf904a/assets/images/character.png"

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the display to start in fullscreen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Pixel Adventure")

def load_and_scale_character_image(url, width, height):
    """
    Downloads and scales the character image from the given URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        character_image_data = BytesIO(response.content)
        character_image = pygame.image.load(character_image_data)
        character_image = pygame.transform.scale(character_image, (width, height))
        return character_image
    else:
        print(f"Error: Unable to download character image from {url}")
        sys.exit()

def update_scaling():
    """
    Updates the scaling factors for character size, speed, gravity, and jump velocity
    based on the current screen dimensions.
    """
    global BASE_SPEED, GRAVITY, character_image, character_rect, ground_level, jump_velocity

    BASE_SPEED = REFERENCE_WIDTH * BASE_SPEED_SCALE * (SCREEN_WIDTH / REFERENCE_WIDTH)
    GRAVITY = REFERENCE_HEIGHT * GRAVITY_SCALE * (SCREEN_HEIGHT / REFERENCE_HEIGHT)
    jump_velocity = -CHARACTER_HEIGHT_PIXELS * JUMP_HEIGHT_MULTIPLIER

    character_image = load_and_scale_character_image(CHARACTER_IMAGE_URL, CHARACTER_WIDTH_PIXELS, CHARACTER_HEIGHT_PIXELS)
    character_rect.size = (CHARACTER_WIDTH_PIXELS, CHARACTER_HEIGHT_PIXELS)
    character_rect.centerx = SCREEN_WIDTH // 2
    character_rect.centery = SCREEN_HEIGHT * 2 // 3
    ground_level = SCREEN_HEIGHT - CHARACTER_HEIGHT_PIXELS

# Initial scaling calculations
BASE_SPEED = REFERENCE_WIDTH * BASE_SPEED_SCALE * (SCREEN_WIDTH / REFERENCE_WIDTH)
GRAVITY = REFERENCE_HEIGHT * GRAVITY_SCALE * (SCREEN_HEIGHT / REFERENCE_HEIGHT)
jump_velocity = -CHARACTER_HEIGHT_PIXELS * JUMP_HEIGHT_MULTIPLIER

# Load and scale character image
character_image = load_and_scale_character_image(CHARACTER_IMAGE_URL, CHARACTER_WIDTH_PIXELS, CHARACTER_HEIGHT_PIXELS)

# Get the rectangle for the character image
character_rect = character_image.get_rect()
character_rect.centerx = SCREEN_WIDTH // 2
character_rect.centery = SCREEN_HEIGHT * 2 // 3

# Vertical speed (velocity)
velocity_y = 0
# Ground level
ground_level = SCREEN_HEIGHT - character_rect.height

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    speed = BASE_SPEED * (SPRINT_MULTIPLIER if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else 1)

    if keys[pygame.K_LEFT]:
        character_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        character_rect.x += speed
    if keys[pygame.K_SPACE] and character_rect.bottom >= ground_level:
        velocity_y = jump_velocity  # Jumping velocity relative to character height

    # Apply gravity
    velocity_y += GRAVITY
    character_rect.y += velocity_y

    # Check if character is on the ground
    if character_rect.bottom >= ground_level:
        character_rect.bottom = ground_level
        velocity_y = 0

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the character
    screen.blit(character_image, character_rect.topleft)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()