import unittest

from fifteen.tile import Tile


class TileTest(unittest.TestCase):
    def test_tiles_with_equal_values_should_be_equal(self):
        self.assertTrue(Tile(1) == Tile(1))
        self.assertFalse(Tile(1) != Tile(1))
    
    def test_tiles_with_not_equal_values_should_not_be_equal(self):
        self.assertFalse(Tile(1) == Tile(2))
        self.assertTrue(Tile(1) != Tile(2))
        
    def test_tile_should_be_equal_to_integer_with_the_same_value(self):
        self.assertTrue(Tile(1) == 1)
        self.assertFalse(Tile(1) != 1)
        
    def test_tile_should_not_be_equal_to_integer_with_different_value(self):
        self.assertFalse(Tile(1) == 2)
        self.assertTrue(Tile(1) != 2)
        
    def test_can_be_compared_with_string(self):
        self.assertEqual('.', Tile('.'))
        self.assertEqual('1', Tile('1'))

    def test_to_string(self):
        self.assertEqual('1', str(Tile(1)))
        self.assertEqual('2', str(Tile(2)))
        self.assertEqual('.', str(Tile('.')))
        
    def test_get_value_1(self):
        tile = Tile(1)
        self.assertEqual(1, tile.get_value())
        
    def test_get_value_2(self):
        tile = Tile(2)
        self.assertEqual(2, tile.get_value())
        
    def test_get_value_3(self):
        tile = Tile('.')
        self.assertEqual('.', tile.get_value())
        
    def test_can_be_highlighted(self):
        tile = Tile(1)
        self.assertFalse(tile.is_highlighted())
        tile.set_highlight(True)
        self.assertTrue(tile.is_highlighted())
        tile.set_highlight(False)
        self.assertFalse(tile.is_highlighted())