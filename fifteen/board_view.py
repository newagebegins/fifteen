import pygame.font

from fifteen.board import Board


class BoardView:
    FONT_SIZE = 50
    FONT_COLOR = (255, 10, 10)
    
    def __init__(self, board, x=0, y=0):
        self._board = board
        self._x = x
        self._y = y
        self._tile_width = self.FONT_SIZE + 10
        self._tile_height = self.FONT_SIZE + 10
        
    def draw(self, surface):
        font = pygame.font.Font(None, self.FONT_SIZE)
        x = self._x
        y = self._y
        for i in range(Board.TILES_COUNT):
            tile = self._board[i]
            
            rect = pygame.Rect(x, y, self._tile_width, self._tile_height)
            rect_width = 1
            if tile.is_highlighted():
                rect_width = 0
            pygame.draw.rect(surface, (0,255,0), rect, rect_width)
            
            if (tile != '.'):
                s = str(tile).rjust(3)
                text = font.render(s, True, self.FONT_COLOR)
                surface.blit(text, (x + 1, y + 13))
            
            if (i + 1) % Board.SIZE == 0:
                x = self._x
                y += self._tile_height
            else:
                x += self._tile_width
    
    def set_tile_width(self, width):
        self._tile_width = width
        
    def set_tile_height(self, height):
        self._tile_height = height
    
    def get_screen_coords_of_tile(self, row, col):
        x = self._x + col * self._tile_width
        y = self._y + row * self._tile_height
        return (x, y)

    def get_tile_at_coords(self, coords):
        x, y = coords
        if x < self._x or y < self._y or x >= self._x + self._get_width() or y >= self._y + self._get_height():
            return None
        row = (y - self._y) / self._tile_height
        col = (x - self._x) / self._tile_width
        return self._board.get_tile(row, col)

    def _get_width(self):
        return Board.SIZE * self._tile_width
    
    def _get_height(self):
        return Board.SIZE * self._tile_height