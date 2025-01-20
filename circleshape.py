import pygame

# Base class for sprites, triangle ship will be circle to make collision easier to detect
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
    # To allow sub-classes override
        pass

    def update(self, dt):
    # TO allow sub-classes override    
        pass