from constants import *
import pygame

def main():
    print("Starting asteroids!")
    print("Screen width: %d\nScreen height: %d" % (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Boot.dev / Asteroids")
    clock = pygame.time.Clock()
    delta = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.flip()
        delta = clock.tick(60) / 1000

if __name__ == "__main__":
    main()