import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame


def main():
    print("Starting asteroids!")
    print("Screen width: %d\nScreen height: %d" % (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Boot.dev / Asteroids")
    clock = pygame.time.Clock()
    delta = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    projectiles = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (projectiles, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")

        for obj in updatable:
            obj.update(delta)
        
        for obj in drawable:
            obj.draw(screen)
        
        for ast in asteroids:
            if player.collision_check(ast):
                print("Game over!")
                sys.exit()
                return

        pygame.display.flip()
        delta = clock.tick(60) / 1000

if __name__ == "__main__":
    main()