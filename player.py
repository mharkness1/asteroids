from circleshape import CircleShape
from constants import *
import pygame
import math
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x ,y, PLAYER_RADIUS)
        self.rotation = 0.0
        self._triangle_points = None
        self.timer = 0

    def triangle(self):
        # Only calculate if rotation has changed
        forward = pygame.Vector2(0, -1).rotate_rad(self.rotation)
        right = forward.rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        # Saving results
        self._triangle_points = [a, b, c]
        
        # Return cached points
        return self._triangle_points
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        rotation_speed = math.radians(PLAYER_TURN_SPEED)
        self.rotation += rotation_speed * dt

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate_rad(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, -1).rotate_rad(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
            else:
                pass
        
        self.timer -= dt