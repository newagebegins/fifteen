import sys

import pygame
from pygame.locals import MOUSEBUTTONDOWN
from pygame.locals import MOUSEMOTION
from pygame.locals import QUIT

from fifteen.board import Board
from fifteen.board_view import BoardView
from fifteen.board_controller import BoardController
from fifteen.game_over_msg import GameOverMessage
from fifteen.button import Button


WINSIZE = [400, 400]


class Game:
    def __init__(self):
        self._board = Board()
        
    def run(self):
        clock = pygame.time.Clock()
        pygame.init()
        screen = pygame.display.set_mode(WINSIZE)
        backbuffer = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
        pygame.display.set_caption('Fifteen')
        
        board = self._board
        board.shuffle()
        board_view = BoardView(board, x=80, y=80)
        board_controller = BoardController(board, board_view)
        game_over_msg = GameOverMessage()
        play_again_btn = Button(title='Play Again', x=80, y=340)
        play_again_btn.attach(self)
    
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    if not board.is_solved():
                        board_controller.mouse_motion(event.pos)
                    else:
                        play_again_btn.mouse_motion(event.pos)
                elif event.type == MOUSEBUTTONDOWN:
                    if not board.is_solved():
                        board_controller.mouse_click(event.pos)
                    else:
                        play_again_btn.mouse_click(event.pos)
            
            backbuffer.fill((0, 0, 0))
            board_view.draw(backbuffer)
            if (board.is_solved()):
                game_over_msg.draw(backbuffer)
                play_again_btn.draw(backbuffer)
            
            screen.blit(backbuffer, (0, 0))
            pygame.display.flip()
            clock.tick(30)
    
    def update(self, subject):
        if isinstance(subject, Button):
            self._board.shuffle()