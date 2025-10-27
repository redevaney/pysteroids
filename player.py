import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOT_SPEED, PLAYER_TURN_SPEED, PLAYER_RADIUS, PLAYER_SPEED,PLAYER_SHOT_COOLDOWN
from shot import Shot 

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = pygame.sprite.Group()
        self.shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]        

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt        

    def shoot(self, dt):
        if self.shot_timer > 0:
            return
        else:
            self.shot_timer = PLAYER_SHOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, pygame.Vector2(0, 0))
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shots.add(shot)
            self.shots.update(dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.position += self.velocity * dt
        self.shot_timer -= dt
        self.shots.update(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

