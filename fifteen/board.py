from fifteen.tile import Tile


class Board:
    SIZE = 4
    TILES_COUNT = SIZE * SIZE
    DEFAULT_BOARD = """
         1  2  3  4
         5  6  7  8
         9 10 11  .
        13 14 12 15
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
        directions = [i + 1, i - 1, i + self.SIZE, i - self.SIZE]
        for d in directions:
            if d >= 0 and d < self.TILES_COUNT and self._tiles[d] == '.':
                self._tiles[i], self._tiles[d] = self._tiles[d], self._tiles[i]
                break
            
    def __iter__(self):
        return self

    def next(self): #@ReservedAssignment
        if self.index == self.TILES_COUNT:
            raise StopIteration
        result = self._tiles[self.index].get_value()
        self.index += 1
        return result

    def __getitem__(self, index):
        return self._tiles[index]
    
    def get_tile(self, row, col):
        return self._tiles[row * self.SIZE + col]