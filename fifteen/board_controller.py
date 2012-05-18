from fifteen.board import Board


class BoardController:  
    def __init__(self, model, view):
        self._model = model
        self._view = view
    
    def mouse_motion(self, mouse_position):
        for i in range(Board.TILES_COUNT):
            self._model[i].set_highlight(False)
        tile = self._view.get_tile_at_coords(mouse_position)
        if tile is not None:
            tile.set_highlight(True)