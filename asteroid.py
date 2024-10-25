import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)

        ast1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        ast2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        ast1.velocity = self.velocity.rotate(rand_angle) * 1.2
        ast2.velocity = self.velocity.rotate(-rand_angle) * 1.2


    def update(self, delta):
        self.position += self.velocity * delta

        if self.position.x < 0 - ASTEROID_MAX_RADIUS or self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS:
            self.kill()

        if self.position.y < 0 - ASTEROID_MAX_RADIUS or self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS:
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    