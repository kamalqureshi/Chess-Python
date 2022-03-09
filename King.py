import Movement

chess = {
    'b_checker': u'\u25FB',
    'b_pawn': u'\u265F',
    'b_rook': u'\u265C',
    'b_knight': u'\u265E',
    'b_bishop': u'\u265D',
    'b_king': u'\u265A',
    'b_queen': u'\u265B',
    'w_checker': u'\u25FC',
    'w_pawn': u'\u2659',
    'w_rook': u'\u2656',
    'w_knight': u'\u2658',
    'w_bishop': u'\u2657',
    'w_king': u'\u2654',
    'w_queen': u'\u2655'
}


class King:

    def __init__(self):
        self.input_coordinates = []
        self.output_coordinates = []

    def setCoordinates(self, input_coordinates, output_coordinates):
        self.output_coordinates = output_coordinates
        self.input_coordinates = input_coordinates

    def possibleMoves(self, board, user, y, x):
        possible_moves = []

        # Possible output 1
        tmp_x = x
        tmp_y = y

        tmp_y = Movement.up(tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible output 2
        tmp_x = x
        tmp_y = y

        tmp_y = Movement.down(tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible Output 3
        tmp_x = x
        tmp_y = y

        tmp_x = Movement.right(tmp_x)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible Output 4
        tmp_x = x
        tmp_y = y

        tmp_x = Movement.left(tmp_x)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible output 5
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible output 6
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible Output 7
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        # Possible Output 8
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_checker'] or \
                    board[tmp_y][tmp_x] == chess['b_checker'] or \
                    board[tmp_y][tmp_x] == '0':
                possible_moves.append([tmp_y, tmp_x])

        return possible_moves

    def __check(self, board, user, x, y):

        # From the current position of the chess piece
        # determine all possible paths and check if
        # at any point it attacks the king. If it down
        # return true else false

        # Possible output 1
        tmp_x = x
        tmp_y = y

        tmp_y = Movement.up(tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible output 2
        tmp_x = x
        tmp_y = y

        tmp_y = Movement.down(tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible Output 3
        tmp_x = x
        tmp_y = y

        tmp_x = Movement.right(tmp_x)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible Output 4
        tmp_x = x
        tmp_y = y

        tmp_x = Movement.left(tmp_x)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible output 5
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible output 6
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible Output 7
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        # Possible Output 8
        tmp_x = x
        tmp_y = y

        tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

        if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king']:
                return True

        return False

    def ValidMove(self, board, user):
        legal = False
        attack = False
        check = False
        moves = Movement

        # Check the output coordinates from the 8
        # possible moves. If one of them matches
        # move the king to the location if there
        # is no other chess piece.

        input_x = self.input_coordinates[1]
        input_y = self.input_coordinates[0]

        output_x = self.output_coordinates[1]
        output_y = self.output_coordinates[0]

        # Possible output 1
        # Move up
        tmp_x = input_x
        tmp_y = input_y

        tmp_y = moves.up(tmp_y)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 2
        # Move down
        tmp_x = input_x
        tmp_y = input_y

        tmp_y = moves.down(tmp_y)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 3
        # Move right
        tmp_x = input_x
        tmp_y = input_y

        tmp_x = moves.right(tmp_x)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 4
        # Move left
        tmp_x = input_x
        tmp_y = input_y

        tmp_x = moves.left(tmp_x)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 5
        # Move right diagonal up
        tmp_x = input_x
        tmp_y = input_y

        tmp_x, tmp_y = moves.right_diagnol_up(tmp_x, tmp_y)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 6
        # Move right diagonal down
        tmp_x = input_x
        tmp_y = input_y

        tmp_x, tmp_y = moves.right_diagnol_down(tmp_x, tmp_y)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 7
        # Move left diagonal up
        tmp_x = input_x
        tmp_y = input_y

        tmp_x, tmp_y = moves.left_diagnol_up(tmp_x, tmp_y)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        # Possible output 8
        # Move left diagonal down
        tmp_x = input_x
        tmp_y = input_y

        tmp_x, tmp_y = moves.left_diagnol_down(tmp_x, tmp_y)
        if tmp_x == output_x and tmp_y == output_y:
            legal = True

            # Check Attack
            if user == 'W':
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = False
                    legal = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = True
            else:
                if board[tmp_y][tmp_x] == '0':
                    attack = False
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_king']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']):
                    attack = True
                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    attack = False
                    legal = False

            check_king = self.__check(board, user, output_x, output_y)
            if check_king:
                legal = True
                check = True
            return legal, attack, check

        return legal, attack, check
