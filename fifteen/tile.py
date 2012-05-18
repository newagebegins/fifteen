class Tile:
    def __init__(self, s):
        if s == '.':
            self._value = s
        else:
            self._value = int(s)
        self._is_highlighted = False
            
    def __eq__(self, other):
        if isinstance(other, Tile):
            return self._value == other._value
        elif isinstance(other, int):
            return self._value == other
        elif isinstance(other, str):
            return str(self._value) == other
    
    def __ne__(self, other):
        return not(self == other)
    
    def __str__(self):
        return str(self._value)
    
    def get_value(self):
        return self._value

    def is_highlighted(self):
        return self._is_highlighted

    def set_highlight(self, value):
        self._is_highlighted = value
