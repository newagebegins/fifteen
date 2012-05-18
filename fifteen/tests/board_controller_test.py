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

    def test_mouse_motion__remove_highlight_when_mouse_leaves_tile_1(self):
        board = Board()
        TILE_POS_1 = {'row': 0, 'col': 0}
        view = BoardView(board)
        controller = BoardController(board, view)
        mouse_position = view.get_screen_coords_of_tile(**TILE_POS_1)
        
        controller.mouse_motion(mouse_position)
        self.assertTrue(board.get_tile(**TILE_POS_1).is_highlighted())
        
        TILE_POS_2 = {'row': 0, 'col': 1}
        mouse_position = view.get_screen_coords_of_tile(**TILE_POS_2)
        controller.mouse_motion(mouse_position)
        self.assertFalse(board.get_tile(**TILE_POS_1).is_highlighted())
        self.assertTrue(board.get_tile(**TILE_POS_2).is_highlighted())
        
    def test_mouse_motion__remove_highlight_when_mouse_leaves_tile_2(self):
        board = Board()
        TILE_POS_1 = {'row': 0, 'col': 1}
        view = BoardView(board)
        controller = BoardController(board, view)
        mouse_position = view.get_screen_coords_of_tile(**TILE_POS_1)
        
        controller.mouse_motion(mouse_position)
        self.assertTrue(board.get_tile(**TILE_POS_1).is_highlighted())
        
        TILE_POS_2 = {'row': 0, 'col': 2}
        mouse_position = view.get_screen_coords_of_tile(**TILE_POS_2)
        controller.mouse_motion(mouse_position)
        self.assertFalse(board.get_tile(**TILE_POS_1).is_highlighted())
        self.assertTrue(board.get_tile(**TILE_POS_2).is_highlighted())
        
    def test_mouse_click__should_move_tile(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board)
        controller = BoardController(board, view)
        mouse_position = view.get_screen_coords_of_tile(row=3, col=3)
        
        controller.mouse_click(mouse_position)
        
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 15
            13 14 12  .
        """)
        self.assertEqual(str(expected), str(board))