import pygame.font

from fifteen.board import Board


class BoardView:
    FONT_SIZE = 45
    FONT_COLOR = (255, 10, 10)
    
    def __init__(self, board, x=0, y=0):
        self._board = board
        self._x = x
        self._y = y
        self._tile_width = self.FONT_SIZE + 15
        self._tile_height = self.FONT_SIZE + 15
        
    def draw(self, surface):
        self._draw_board(surface)
        self._draw_tiles(surface)
                
    def _draw_board(self, surface):
        color = (0,255,0)
        pygame.draw.rect(surface, color, self._get_rect(), 1)
        
        for i in range(Board.SIZE):
            # Horizontal lines.
            pt_start = (self._x, self._y + self._tile_height * i)
            pt_end = (self._x + self._get_width() - 1,
                      self._y + self._tile_height * i)
            pygame.draw.line(surface, color, pt_start, pt_end)
            # Vertical lines.
            pt_start = (self._x + self._tile_width * i, self._y)
            pt_end = (self._x + self._tile_width * i,
                      self._y + self._get_height() - 1)
            pygame.draw.line(surface, color, pt_start, pt_end)\
            
    def _draw_tiles(self, surface):
        font = pygame.font.Font('freesansbold.ttf', self.FONT_SIZE)
        x = self._x
        y = self._y
        for i in range(Board.TILES_COUNT):
            tile = self._board[i]
            
            rect = pygame.Rect(x, y, self._tile_width, self._tile_height)
            if tile.is_highlighted():
                pygame.draw.rect(surface, (0,255,0), rect, 0)
            
            if (tile != '.'):
                s = str(tile).rjust(3)
                text = font.render(s, True, self.FONT_COLOR)
                surface.blit(text, (x - 7, y + 13))
            
            if (i + 1) % Board.SIZE == 0:
                x = self._x
                y += self._tile_height
            else:
                x += self._tile_width
        
    def _get_rect(self):
        '''Return a bounding rectangle in which the board resides'''
        return pygame.Rect(self._x,
                           self._y,
                           self._get_width(),
                           self._get_height())
    
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
        if not self._get_rect().collidepoint(coords):
            return None
        row = (y - self._y) / self._tile_height
        col = (x - self._x) / self._tile_width
        return self._board.get_tile(row, col)

    def _get_width(self):
        return Board.SIZE * self._tile_width
    
    def _get_height(self):
        return Board.SIZE * self._tile_height