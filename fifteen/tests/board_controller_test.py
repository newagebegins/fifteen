import unittest

from fifteen.board import Board
from fifteen.board_view import BoardView
from fifteen.board_controller import BoardController


class BoardControllerTest(unittest.TestCase):
    def test_mouse_motion__highlight_tile_when_mouse_is_over_that_tile(self):
        board = Board()
        TILE_POS = {'row': 0, 'col': 0}
        tile = board.get_tile(**TILE_POS)
        view = BoardView(board)
        controller = BoardController(board, view)
        mouse_position = view.get_screen_coords_of_tile(**TILE_POS)
        
        self.assertFalse(tile.is_highlighted())
        controller.mouse_motion(mouse_position)
        self.assertTrue(tile.is_highlighted())
        
    def test_mouse_motion__do_not_throw_exception_when_mouse_is_not_over_the_board(self):
        board = Board()
        view = BoardView(board)
        controller = BoardController(board, view)
        controller.mouse_motion((999, 999))
