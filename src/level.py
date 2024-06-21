import pygame
from settings import *
from player import Player
from enemy import Enemy
from laser import Laser

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, is_ground=False):
        """
        Initialize a platform with a given position and size.

        Parameters:
            x (int): The x-coordinate of the platform.
            y (int): The y-coordinate of the platform.
            width (int): The width of the platform.
            height (int): The height of the platform.
            is_ground (bool): Flag indicating if this platform is the ground.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_ground = is_ground  # Flag to identify the ground platform

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """
        Initialize a door with a given position and size.

        Parameters:
            x (int): The x-coordinate of the door.
            y (int): The y-coordinate of the door.
            width (int): The width of the door.
            height (int): The height of the door.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Green color for the door
        self.rect = self.image.get_rect(topleft=(x, y))

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Initialize a collectible with a given position.

        Parameters:
            x (int): The x-coordinate of the collectible.
            y (int): The y-coordinate of the collectible.
        """
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Size of the collectible
        self.image.fill((255, 215, 0))  # Gold color for the collectible
        self.rect = self.image.get_rect(center=(x, y))

class Level:
    def __init__(self):
        """
        Initialize the level by creating platforms, enemies, collectibles, and a door.
        """
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.door = None
        self.load_level()

    def load_level(self):
        """
        Load the level by defining platforms, enemies, and the door with relative positioning.
        """
        screen_height = SCREEN_HEIGHT
        screen_width = SCREEN_WIDTH
        player_height = PLAYER_HEIGHT
        platform_height = player_height // 5
        platform_width_small = screen_width // 8  # Platforms are an eighth of the screen width
        platform_width_medium = screen_width // 4  # Platforms are a quarter of the screen width
        platform_width_large = screen_width // 2  # Platforms are half of the screen width

        # Define platforms with relative positioning
        platforms_data = [
            (screen_width // 10, screen_height - player_height * 2, platform_width_medium, platform_height),
            (screen_width // 2, screen_height - player_height * 5, platform_width_medium, platform_height),
            (screen_width // 14, screen_height - player_height * 6.5, platform_width_small, platform_height),
            (screen_width // 2, screen_height - player_height * 8, platform_width_large, platform_height),
            (0, screen_height - TILE_SIZE, screen_width, TILE_SIZE),  # Ground
        ]

        # Create and add platforms to the platforms group
        for i, (x, y, width, height) in enumerate(platforms_data):
            is_ground = i == len(platforms_data) - 1  # The last platform is the ground
            platform = Platform(x, y, width, height, is_ground=is_ground)
            self.platforms.add(platform)

            # Add enemies on the medium platforms
            if width == platform_width_medium:
                enemy = Enemy(x + width // 2, y - 20)  # Centered and slightly above the platform
                self.enemies.add(enemy)

            # Add a collectible to the small platform
            if width == platform_width_small:
                collectible = Collectible(x + width // 2, y - 15)  # Centered and slightly above the platform
                self.collectibles.add(collectible)

        # Create and position the door
        door_width = 120
        door_height = 120
        self.door = Door(screen_width // 2 - door_width // 2, screen_height - TILE_SIZE - door_height, door_width, door_height)

    def draw(self, screen, camera_offset):
        """
        Draw the platforms, the door, enemies, lasers, and collectibles on the screen with a camera offset.

        Parameters:
            screen (pygame.Surface): The game screen to draw on.
            camera_offset (tuple): The camera offset for drawing the level.
        """
        # Draw each platform with the camera offset
        for platform in self.platforms:
            screen.blit(platform.image, (platform.rect.x - camera_offset[0], platform.rect.y - camera_offset[1]))
        # Draw each enemy with the camera offset
        for enemy in self.enemies:
            screen.blit(enemy.image, (enemy.rect.x - camera_offset[0], enemy.rect.y - camera_offset[1]))
        # Draw each laser with the camera offset
        for laser in self.lasers:
            screen.blit(laser.image, (laser.rect.x - camera_offset[0], laser.rect.y - camera_offset[1]))
        # Draw each collectible with the camera offset
        for collectible in self.collectibles:
            screen.blit(collectible.image, (collectible.rect.x - camera_offset[0], collectible.rect.y - camera_offset[1]))
        # Draw the door with the camera offset
        if self.door:
            screen.blit(self.door.image, (self.door.rect.x - camera_offset[0], self.door.rect.y - camera_offset[1]))

    def update(self):
        """
        Update enemies, lasers, and handle shooting logic.
        """
        for enemy in self.enemies:
            lasers = enemy.update()
            for laser in lasers:
                self.lasers.add(laser)
        self.lasers.update()

    def get_platforms(self):
        """
        Get the group of platforms in the level.

        Returns:
            pygame.sprite.Group: The group of platforms.
        """
        return self.platforms

    def get_door(self):
        """
        Get the door in the level.

        Returns:
            Door: The door object.
        """
        return self.door

    def get_collectibles(self):
        """
        Get the group of collectibles in the level.

        Returns:
            pygame.sprite.Group: The group of collectibles.
        """
        return self.collectibles

    def get_lasers(self):
        """
        Get the group of lasers in the level.

        Returns:
            pygame.sprite.Group: The group of lasers.
        """
        return self.lasers

    def get_enemies(self):
        """
        Get the group of enemies in the level.

        Returns:
            pygame.sprite.Group: The group of enemies.
        """
        return self.enemies
