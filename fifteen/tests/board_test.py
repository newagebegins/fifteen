import unittest

from fifteen.board import Board


class BoardTest(unittest.TestCase):
    def test_board_as_string(self):
        board = Board("""
            1  5  9 13
            2  6 10 14
            3  7 11 15
            4  8  . 12
        """)
        expected =\
            "  1  5  9 13\n" +\
            "  2  6 10 14\n" +\
            "  3  7 11 15\n" +\
            "  4  8  . 12"
        self.assertEqual(expected, str(board))
        
    def test_move_1(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        board.move(15)
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14  . 15
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_move_2(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        board.move(12)
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 15 12
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_move_3(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14  . 15
        """)
        board.move(15)
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_move_4(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        board.move(1)
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_move_5(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        board.move(15)
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 15
            13 14 12  .
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_move_6(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        board.move(4)
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15  .
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_iterator(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        actual = []
        for tile in board:
            actual.append(tile)
        expected = [1,2,3,4,5,6,7,8,9,10,11,'.',13,14,12,15]
        self.assertEqual(expected, actual)
        
    def test_board_as_array_of_tiles(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        self.assertEqual(1, board[0])
        self.assertEqual(15, board[15])
        
    def test_default_constructor(self):
        board = Board()
        expected = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        self.assertEqual(str(expected), str(board))
        
    def test_get_tile(self):
        board = Board("""
             1  2  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        self.assertEqual(7, board.get_tile(row=1, col=2))
        self.assertEqual(15, board.get_tile(row=3, col=3))