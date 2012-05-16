class Board:
    SIZE = 4
    TILES_COUNT = SIZE * SIZE

    def __init__(self, s):
        self._tiles = s.split()        
        
    def __str__(self):
        result = ''
        for i in range(len(self._tiles)):
            if i != 0 and i % self.SIZE == 0:
                result += '\n'
            result += self._tiles[i].rjust(3)
        return result

    def move(self, tile):
        i = self._tiles.index(str(tile))
        directions = [i + 1, i - 1, i + self.SIZE, i - self.SIZE]
        for d in directions:
            if d >= 0 and d < self.TILES_COUNT and self._tiles[d] == '.':
                self._tiles[i], self._tiles[d] = self._tiles[d], self._tiles[i]
                break