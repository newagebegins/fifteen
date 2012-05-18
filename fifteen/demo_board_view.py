from fifteen.game import Game
from fifteen.board import Board


class DemoBoardView(Game):
    def _get_board(self):
        board = Board("""
             2  1  3  4
             5  6  7  8
             9 10 11  .
            13 14 12 15
        """)
        board.get_tile(0, 0).set_highlight(True)
        return board
    
    def _should_handle_mouse(self):
        return False
        
if __name__ == '__main__':
    DemoBoardView().run()