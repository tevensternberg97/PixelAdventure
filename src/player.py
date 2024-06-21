import pygame
from settings import *
from highscore import update_highscore

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load and scale the player image
        self.image = pygame.image.load(LOCAL_CHARACTER_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        # Initialize player position at the center top of the screen
        self.rect.center = (SCREEN_WIDTH // 2, PLAYER_HEIGHT // 2)
        # Initialize speed and state variables
        self.speed_x = 0
        self.speed_y = 0
        self.on_ground = True
        self.dropping = False  # Variable to track if the player is dropping through a platform
        self.current_platform = None  # Store the current platform the player is standing on
        # Store the starting position for respawn
        self.start_position = self.rect.center
        self.score = 0  # Initialize player score
        self.start_time = pygame.time.get_ticks()  # Store the start time

    def update(self, level):
        """
        Update the player's position and handle collisions.
        """
        # Update player position based on speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Apply gravity if the player is not on the ground
        if not self.on_ground:
            self.speed_y += GRAVITY
        # Check for collisions with platforms
        self.check_vertical_collisions(level)
        self.check_horizontal_collisions(level)
        # Check for interactions with the door
        self.check_door(level.get_door())
        # Check if the player falls below the ground
        self.check_death()
        # Check for collisions with collectibles
        self.check_collectibles(level.get_collectibles())
        # Check for collisions with lasers
        self.check_lasers(level.get_lasers())
        # Check for collisions with enemies
        self.check_enemies(level.get_enemies())

    def check_vertical_collisions(self, level):
        """
        Check for vertical collisions with platforms.
        """
        self.on_ground = False
        for platform in level.get_platforms():
            if self.rect.colliderect(platform.rect):
                if self.dropping and self.current_platform == platform:
                    # Skip collision if dropping through the current platform
                    continue
                if self.speed_y > 0 and self.rect.bottom <= platform.rect.top + self.speed_y:
                    self.rect.bottom = platform.rect.top
                    self.speed_y = 0
                    self.on_ground = True
                    self.current_platform = platform  # Set the current platform
                    self.dropping = False  # Reset dropping state after landing
                elif self.speed_y < 0 and self.rect.top >= platform.rect.bottom:
                    continue

    def check_horizontal_collisions(self, level):
        """
        Check for horizontal collisions with platforms.
        """
        if self.on_ground:
            for platform in level.get_platforms():
                if self.rect.colliderect(platform.rect):
                    if self.rect.right > platform.rect.left and self.rect.left < platform.rect.right:
                        if self.speed_x > 0:
                            self.rect.right = platform.rect.left
                        elif self.speed_x < 0:
                            self.rect.left = platform.rect.right
                        self.speed_x = 0

    def check_door(self, door):
        """
        Check if the player collides with the door and interacts with it.
        """
        if self.rect.colliderect(door.rect):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                print("Level Complete!")
                self.complete_level()

    def complete_level(self):
        """
        Handle level completion logic.
        """
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000  # Time in seconds
        score_multiplier = max(1, 1000 - elapsed_time)  # Example scoring logic
        self.score += score_multiplier
        update_highscore("1", self.score)  # Update high score for level 1
        from main import show_level_complete_ui
        show_level_complete_ui()

    def check_death(self):
        """
        Check if the player falls below the ground level.
        """
        if self.rect.top > SCREEN_HEIGHT:
            print("You died! Respawning...")
            self.respawn()

    def respawn(self):
        """
        Respawn the player at the starting position.
        """
        self.rect.center = self.start_position
        self.speed_x = 0
        self.speed_y = 0

    def jump(self):
        """
        Make the player jump if they are on the ground.
        """
        if self.on_ground:
            self.speed_y = -JUMP_HEIGHT
            self.on_ground = False
            print("Jump!")

    def drop(self):
        """
        Allow the player to drop through platforms.
        """
        if self.on_ground and self.current_platform is not None and not self.current_platform.is_ground:
            self.dropping = True
            self.rect.y += 1  # Move the player down slightly to start dropping through the platform
            self.on_ground = False
            self.current_platform = None  # Reset current platform to ensure dropping through only one platform
            print("Drop!")

    def check_collectibles(self, collectibles):
        """
        Check if the player collides with any collectibles.
        """
        collected = pygame.sprite.spritecollide(self, collectibles, True)
        if collected:
            print("Collected an item!")
            self.score += 100  # Example bonus score for collecting an item

    def check_lasers(self, lasers):
        """
        Check if the player collides with any lasers.
        """
        for laser in lasers:
            if self.rect.colliderect(laser.rect):
                if self.rect.bottom <= laser.rect.top:
                    # Player jumps on the laser from the top
                    print("Laser destroyed!")
                    laser.kill()
                    self.score += 50  # Example score for destroying a laser
                else:
                    # Player hit by the laser
                    print("Hit by laser! Respawning...")
                    self.respawn()

    def check_enemies(self, enemies):
        """
        Check if the player collides with any enemies.
        """
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if self.rect.bottom <= enemy.rect.top + 10:  # Allow some tolerance for jumping on top
                    # Player jumps on the enemy from the top
                    print("Enemy defeated!")
                    enemy.kill()
                    self.score += 150  # Example score for defeating an enemy
                    self.speed_y = -JUMP_HEIGHT  # Bounce up after defeating an enemy
                else:
                    # Player hit by the enemy
                    print("Hit by enemy! Respawning...")
                    self.respawn()
