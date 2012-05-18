from fifteen.board import Board


class BoardController:  
    def __init__(self, model, view):
        self._model = model
        self._view = view
    
    def mouse_motion(self, mouse_position):
        self._highlight_tile_at_coords(mouse_position)
    
    def mouse_click(self, mouse_position):
        self._move_tile_at_coords(mouse_position)
        self._highlight_tile_at_coords(mouse_position)
            
    def _highlight_tile_at_coords(self, coords):
        self._remove_highlight_for_all_tiles()
        tile = self._view.get_tile_at_coords(coords)
        if tile is not None:
            tile.set_highlight(True)
            
    def _remove_highlight_for_all_tiles(self):
        for i in range(Board.TILES_COUNT):
            self._model[i].set_highlight(False)
            
    def _move_tile_at_coords(self, coords):
        tile = self._view.get_tile_at_coords(coords)
        if tile is not None:
            self._model.move(tile)