class BoardController:  
    def __init__(self, model, view):
        self._model = model
        self._view = view
    
    def mouse_motion(self, mouse_position):
        tile = self._view.get_tile_at_coords(mouse_position)
        if tile is not None:
            tile.set_highlight(True)
