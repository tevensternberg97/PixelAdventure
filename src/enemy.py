import pygame
from laser import Laser

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Initialize an enemy with a given position.

        Parameters:
            x (int): The x-coordinate of the enemy.
            y (int): The y-coordinate of the enemy.
        """
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Size of the enemy
        self.image.fill((255, 0, 0))  # Red color for the enemy
        self.rect = self.image.get_rect(center=(x, y))
        self.last_shot_time = pygame.time.get_ticks()  # Time of the last shot

    def update(self):
        """
        Update the enemy and shoot lasers in all directions every 3 seconds.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 3000:  # Shoot every 3 seconds
            self.last_shot_time = current_time
            return [
                Laser(self.rect.centerx, self.rect.centery, 'up'),
                Laser(self.rect.centerx, self.rect.centery, 'down'),
                Laser(self.rect.centerx, self.rect.centery, 'left'),
                Laser(self.rect.centerx, self.rect.centery, 'right')
            ]
        return []
