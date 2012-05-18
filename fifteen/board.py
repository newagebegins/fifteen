import random

from fifteen.tile import Tile


class Board:
    SIZE = 4
    TILES_COUNT = SIZE * SIZE
    DEFAULT_BOARD = """
         1  2  3  4
         5  6  7  8
         9 10 11 12
        13 14  . 15
    """
    
    def __init__(self, s=DEFAULT_BOARD):
        self._tiles = map(self._create_tile_from_string, s.split())
        self.index = 0
        
    def _create_tile_from_string(self, s):
        return Tile(s)
        
    def __str__(self):
        result = ''
        for i in range(len(self._tiles)):
            if i != 0 and i % self.SIZE == 0:
                result += '\n'
            result += str(self._tiles[i]).rjust(3)
        return result

    def move(self, tile):
        i = self._tiles.index(tile)
        j = self._get_possible_move_for_tile(tile)
        if j is not None:
            self._tiles[i], self._tiles[j] = self._tiles[j], self._tiles[i]
            
    def _get_possible_move_for_tile(self, tile):
        '''
        For given tile return index of empty adjacent or None if such a tile is
        not found
        '''
        i = self._tiles.index(tile)
        directions = [i + 1, i - 1, i + self.SIZE, i - self.SIZE]
        for d in directions:
            if d >= 0 and d < self.TILES_COUNT and self._tiles[d] == '.':
                return d
        return None
    
    def __iter__(self):
        return self

    def next(self): #@ReservedAssignment
        if self.index == self.TILES_COUNT:
            raise StopIteration
        result = self._tiles[self.index]
        self.index += 1
        return result

    def __getitem__(self, index):
        return self._tiles[index]
    
    def get_tile(self, row, col):
        return self._tiles[row * self.SIZE + col]
    
    def is_solved(self):
        solved_board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        return str(self) == str(solved_board)
    
    def is_tile_movable(self, tile):
        return self._get_possible_move_for_tile(tile) is not None

    def get_movable_tiles(self):
        return [x for x in self._tiles if self.is_tile_movable(x)]

    def shuffle(self):
        moves = 100
        while moves > 0 or self.is_solved():
            tiles = self.get_movable_tiles()
            self.move(random.choice(tiles))
            moves -= 1