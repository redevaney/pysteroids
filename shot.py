import pygame
from constants import SHOT_RADIUS,PLAYER_SHOT_SPEED
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(direction) * PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        # Remove the shot if it goes off-screen
        if (self.position.x < 0 or self.position.x > 1280 or
            self.position.y < 0 or self.position.y > 720):
            self.kill()