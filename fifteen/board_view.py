import pygame.font
from fifteen.board import Board

class BoardView:
    def __init__(self, board):
        self._board = board
        
    def draw(self, surface):
        font = pygame.font.Font(None, 36)
        x = 0
        y = 0
        for i in range(Board.TILES_COUNT):
            if (self._board[i] != '.'):
                s = str(self._board[i]).rjust(3)
                text = font.render(s, True, (255, 10, 10))
                surface.blit(text, (x, y))
            if (i + 1) % Board.SIZE == 0:
                x = 0
                y += 40
            else:
                x += 40