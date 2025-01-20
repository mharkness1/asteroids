from circleshape import CircleShape
from constants import *
import pygame
import math

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x ,y, PLAYER_RADIUS)
        self.rotation = 0.0
        self._triangle_points = None
        self._last_rotation = None

    def triangle(self):
        # Only calculate if rotation has changed
        if self._last_rotation != self.rotation:

            forward = pygame.Vector2(0, -1).rotate_rad(self.rotation)
            right = forward.rotate(90) * self.radius / 1.5
            a = self.position + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            # Saving results
            self._triangle_points = [a, b, c]
            # Updating comparison for the main loop
            self._last_rotation = self.rotation
        # Return cached points
        return self._triangle_points
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        rotation_speed = math.radians(PLAYER_TURN_SPEED)
        self.rotation += rotation_speed * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)