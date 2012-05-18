import unittest

from fifteen.board_view import BoardView
from fifteen.board import Board


class BoardViewTest(unittest.TestCase):
    def test_get_screen_coords_of_tile_1(self):
        board = Board()
        board_view = BoardView(board, x=0, y=0)
        coords = board_view.get_screen_coords_of_tile(row=0, col=0)
        self.assertEqual((0, 0), coords)
        
    def test_get_screen_coords_of_tile_2(self):
        board = Board()
        board_view = BoardView(board, x=0, y=0)
        board_view.set_tile_width(10)
        coords = board_view.get_screen_coords_of_tile(row=0, col=1)
        self.assertEqual((10, 0), coords)
        
    def test_get_screen_coords_of_tile_3(self):
        board = Board()
        board_view = BoardView(board, x=0, y=0)
        board_view.set_tile_height(10)
        coords = board_view.get_screen_coords_of_tile(row=1, col=0)
        self.assertEqual((0, 10), coords)
        
    def test_get_screen_coords_of_tile_4(self):
        board = Board()
        board_view = BoardView(board, x=0, y=0)
        board_view.set_tile_width(10)
        board_view.set_tile_height(20)
        coords = board_view.get_screen_coords_of_tile(row=3, col=2)
        self.assertEqual((20, 60), coords)
        
    def test_get_screen_coords_of_tile_5(self):
        board = Board()
        board_view = BoardView(board, x=10, y=20)
        board_view.set_tile_width(10)
        board_view.set_tile_height(20)
        coords = board_view.get_screen_coords_of_tile(row=3, col=2)
        self.assertEqual((30, 80), coords)
        
    def test_get_tile_at_coords_1(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        self.assertEqual(1, view.get_tile_at_coords((0, 0)))
        
    def test_get_tile_at_coords_2(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        self.assertEqual(2, view.get_tile_at_coords((0, 0)))
        
    def test_get_tile_at_coords_3(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        view.set_tile_width(10)
        self.assertEqual(1, view.get_tile_at_coords((10, 0)))
        
    def test_get_tile_at_coords_4(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        view.set_tile_height(10)
        self.assertEqual(5, view.get_tile_at_coords((0, 10)))
        
    def test_get_tile_at_coords_5(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=10, y=20)
        view.set_tile_width(10)
        view.set_tile_height(10)
        self.assertEqual(6, view.get_tile_at_coords((20, 30)))
        
    def test_get_tile_at_coords_6(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        view.set_tile_width(10)
        view.set_tile_height(10)
        self.assertEqual(1, view.get_tile_at_coords((11, 0)))
        self.assertEqual(1, view.get_tile_at_coords((19, 0)))
        self.assertEqual(3, view.get_tile_at_coords((20, 0)))
        self.assertEqual(1, view.get_tile_at_coords((19, 9)))
        self.assertEqual(6, view.get_tile_at_coords((19, 10)))
        
    def test_get_tile_at_coords__if_no_tile_with_coords_exist__return_none_1(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        view.set_tile_width(1)
        view.set_tile_height(1)
        self.assertEqual(None, view.get_tile_at_coords((-1, 0)))
        
    def test_get_tile_at_coords__if_no_tile_with_coords_exist__return_none_2(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=10, y=0)
        view.set_tile_width(1)
        view.set_tile_height(1)
        self.assertEqual(None, view.get_tile_at_coords((9, 0)))
        
    def test_get_tile_at_coords__if_no_tile_with_coords_exist__return_none_3(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        view.set_tile_width(1)
        view.set_tile_height(1)
        self.assertEqual(None, view.get_tile_at_coords((0, -1)))
        
    def test_get_tile_at_coords__if_no_tile_with_coords_exist__return_none_4(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=10)
        view.set_tile_width(1)
        view.set_tile_height(1)
        self.assertEqual(None, view.get_tile_at_coords((0, 9)))
        
    def test_get_tile_at_coords__if_no_tile_with_coords_exist__return_none_5(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        view = BoardView(board, x=0, y=0)
        view.set_tile_width(1)
        view.set_tile_height(1)
        self.assertEqual(4, view.get_tile_at_coords((3, 0)))
        self.assertEqual(None, view.get_tile_at_coords((4, 0)))
        self.assertEqual(None, view.get_tile_at_coords((999, 0)))
        self.assertEqual(13, view.get_tile_at_coords((0, 3)))
        self.assertEqual(None, view.get_tile_at_coords((0, 4)))
        self.assertEqual(None, view.get_tile_at_coords((0, 999)))
        self.assertEqual(None, view.get_tile_at_coords((999, 999)))
        self.assertEqual(None, view.get_tile_at_coords((-1, -1)))