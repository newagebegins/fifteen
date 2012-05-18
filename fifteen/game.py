import sys

import pygame
from pygame.locals import MOUSEBUTTONDOWN
from pygame.locals import MOUSEMOTION
from pygame.locals import QUIT

from fifteen.board import Board
from fifteen.board_view import BoardView
from fifteen.board_controller import BoardController


WINSIZE = [640, 480]


class Game:
    def run(self):
        clock = pygame.time.Clock()
        pygame.init()
        screen = pygame.display.set_mode(WINSIZE)
        backbuffer = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
        pygame.display.set_caption('Fifteen')
        
        board = self._get_board()
        board_view = BoardView(board, x=50, y=50)
        board_controller = BoardController(board, board_view)
    
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION and self._should_handle_mouse():
                    board_controller.mouse_motion(event.pos)
                elif event.type == MOUSEBUTTONDOWN and self._should_handle_mouse():
                    board_controller.mouse_click(event.pos)
            
            backbuffer.fill((0, 0, 0))
            board_view.draw(backbuffer)
            
            screen.blit(backbuffer, (0, 0))
            pygame.display.flip()
            clock.tick(30)
            
    def _get_board(self):
        board = Board()
        board.shuffle()
        return board
        
    def _should_handle_mouse(self):
        return True