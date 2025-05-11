import pygame.draw
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # Handles splitting when shot
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child1_rot = self.velocity.rotate(random_angle)
        child2_rot = self.velocity.rotate(-random_angle)
        child1 = Asteroid(self.position[0], self.position[1], new_radius)
        child2 = Asteroid(self.position[0], self.position[1], new_radius)
        child1.velocity = child1_rot * 1.2
        child2.velocity = child2_rot * 1.2