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
