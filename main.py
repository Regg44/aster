import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    dt = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill("black")
        
        for p in updatable:
            p.update(dt)
        
        for a in asteroids:
            if a.collision(player):
                print("Game Over!")
                return
            for b in bullets:
                if b.collision(a):
                    a.split()
                    b.kill()
        for p in drawable:
            p.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

    
if __name__ == "__main__":
    main()