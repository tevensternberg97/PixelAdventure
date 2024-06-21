import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        """
        Initialize a laser with a given position and direction.

        Parameters:
            x (int): The x-coordinate of the laser.
            y (int): The y-coordinate of the laser.
            direction (str): The direction of the laser ('up', 'down', 'left', 'right').
        """
        super().__init__()
        if direction in ['up', 'down']:
            self.image = pygame.Surface((5, 20))  # Size of the laser for vertical movement
        else:
            self.image = pygame.Surface((20, 5))  # Size of the laser for horizontal movement
        self.image.fill((255, 0, 0))  # Red color for the laser
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 5  # Speed of the laser

    def update(self):
        """
        Update the laser's position.
        """
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0 or self.rect.left > SCREEN_WIDTH or self.rect.right < 0:
            self.kill()  # Remove the laser when it goes off screen
