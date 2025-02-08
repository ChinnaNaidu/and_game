import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        #player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000, rect=None, special_flags=0)
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over")
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid):
                    asteroid.kill()
                    shot.kill()
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__" :
    main()

