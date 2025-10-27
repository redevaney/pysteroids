import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = updatables, drawables
    Asteroid.containers = updatables, drawables, asteroids
    AsteroidField.containers = updatables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        updatables.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                pygame.quit()
                return

        player.shots.update(dt)
        for shot in player.shots:
            shot.draw(screen)
        for asteroid in asteroids:
            for shot in player.shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
