import sys

import pygame
from pygame.locals import QUIT

from fifteen.board import Board
from fifteen.board_view import BoardView


WINSIZE = [640, 480]


def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    backbuffer = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    pygame.display.set_caption('Fifteen')
    
    board = Board("""
         1  2  3  4
         5  6  7  8
         9 10 11  .
        13 14 12 15
    """)
    board_view = BoardView(board)

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
             
        board_view.draw(backbuffer)
        
        screen.blit(backbuffer, (0, 0))
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
