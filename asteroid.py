import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        new_direction = random.uniform(20,50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            new_asteroid_left = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_right = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_left.velocity = self.velocity.rotate(new_direction * 1.2)
            new_asteroid_right.velocity = self.velocity.rotate(new_direction * -1.2)
            self.kill()
