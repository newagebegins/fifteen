import pygame.font

from fifteen.board import Board


class BoardView:
    FONT_SIZE = 50
    FONT_COLOR = (255, 10, 10)
    
    TILE_WIDTH = FONT_SIZE + 10
    TILE_HEIGHT = FONT_SIZE + 10
    
    def __init__(self, board, x, y):
        self._board = board
        self._x = x
        self._y = y
        self._font = pygame.font.Font(None, self.FONT_SIZE)
        
    def draw(self, surface):
        x = self._x
        y = self._y
        for i in range(Board.TILES_COUNT):
            if (self._board[i] != '.'):
                s = str(self._board[i]).rjust(3)
                text = self._font.render(s, True, self.FONT_COLOR)
                surface.blit(text, (x + 1, y + 13))
                
            rect = pygame.Rect(x, y, self.TILE_WIDTH, self.TILE_HEIGHT)
            pygame.draw.rect(surface, self.FONT_COLOR, rect, 1)
            
            if (i + 1) % Board.SIZE == 0:
                x = self._x
                y += self.TILE_HEIGHT
            else:
                x += self.TILE_WIDTH