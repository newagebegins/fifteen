class Board:
    SIZE = 4
    TILES_COUNT = SIZE * SIZE

    def __init__(self, s):
        self._tiles = map(self._convert_tile_to_int, s.split())
        self.index = 0
        
    def _convert_tile_to_int(self, tile):
        if tile == '.':
            return tile
        return int(tile)
        
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
        result = self._tiles[self.index]
        self.index += 1
        return result

    def __getitem__(self, index):
        return self._tiles[index]