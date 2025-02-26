from circleshape import *
from constants import *
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(angle)
        vect2 = self.velocity.rotate(angle*(-1))
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        sma1 = Asteroid(self.position.x, self.position.y, new_rad)
        sma1.velocity = vect1 * 1.2
        sma2 = Asteroid(self.position.x, self.position.y, new_rad)
        sma2.velocity = vect2 * 1.2
        
        
        