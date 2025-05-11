import pygame
import sys

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Start of initialisation process
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time

    # Creation of groups
    updatable = pygame.sprite.Group() # Group for storing all objects that should be updates
    drawable = pygame.sprite.Group() # Group for storing all objects that should be rendered
    asteroids = pygame.sprite.Group() # Group for storing all asteroids
    shots = pygame.sprite.Group() #  Group for storing all bullets

    # Creation of player
    Player.containers = (updatable, drawable) # Makes all instances of player class in the two groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Creates player in the middle of the screen

    # Creation of asteroids
    Asteroid.containers = (updatable, drawable, asteroids)

    # Creation of asteroid field
    AsteroidField.containers = updatable
    AsteroidField()

    # Creation of shots
    Shot.containers = (updatable, drawable, shots)

    # Start of game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #making the close button on window work
                return
        screen.fill((0,0,0)) #filling frame with full black
        updatable.update(dt) # Calls update() on every object in updatable group
        for asteroid in asteroids:
            if asteroid.collide(player): # Checks if any asteroid collides with player
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
        for obj in drawable: # Iterates over drawable group and calls draw() on every object
            obj.draw(screen)
        time = clock.tick(60) #waiting for 1/60th of a second
        dt = time / 1000.0 # calculating delta time in seconds
        pygame.display.flip() #rendering the frame

if __name__ == "__main__":
    main()