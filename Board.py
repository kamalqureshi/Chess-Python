class Board:
    board = [['  ' for i in range(8) for i in range(8)]]
    board = [[' bR ', ' bK ', ' bB ', ' bQ ', ' bK ', ' bR ', ' bK ', ' bB '],
             [' bP ', ' bP ', ' bP ', ' bP ', ' bP ', ' bP ', ' bP ', ' bP '],
             [' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- '],
             [' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- '],
             [' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- '],
             [' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- ', ' -- '],
             [' wP ', ' wP ', ' wP ', ' wP ', ' wP ', ' wP ', ' wP ', ' wP '],
             [' wR ', ' wK ', ' wB ', ' wQ ', ' wK ', ' wR ', ' wK ', ' wB ']]

    def displayboard(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                print(self.board[r][c], end=' ')
            print()
