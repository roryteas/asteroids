import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)    
    Shot.containers = (shots, updateable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updateable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print('Game over!')
                return

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) /1000

    return

if __name__ == "__main__":
    main()
