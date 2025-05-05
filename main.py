import pygame

from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #making the close button on window work
                return
        screen.fill((0,0,0)) #filling frame with full black
        pygame.display.flip() #rendering the frame
        time = clock.tick(60) #waiting for 1/60th of a second
        dt = time / 1000.0 # calculating delta time in seconds

if __name__ == "__main__":
    main()