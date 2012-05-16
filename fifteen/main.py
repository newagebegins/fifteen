import sys
import pygame
from pygame.locals import * #@UnusedWildImport

def main():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_mode([640, 480])
    pygame.display.set_caption('Fifteen')

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
