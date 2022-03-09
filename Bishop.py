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


class Bishop:

    def __init__(self):
        self.input_coordinates = []
        self.output_coordinates = []

    def setCoordinates(self, input_coordinates, output_coordinates):
        self.output_coordinates = output_coordinates
        self.input_coordinates = input_coordinates

    def possibleMoves(self, board, user, y, x):
        possible_moves = []

        # From the current position of the chess piece
        # determine all possible paths and append them
        # to a list

        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

        while 8 > tmp_x >= 0 and 8 > tmp_y >= 0:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

            elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                 or board[tmp_y][tmp_x] == chess['b_rook']
                                                 or board[tmp_y][tmp_x] == chess['b_knight']
                                                 or board[tmp_y][tmp_x] == chess['b_bishop']
                                                 or board[tmp_y][tmp_x] == chess['b_queen']
                                                 or board[tmp_y][tmp_x] == chess['w_pawn']
                                                 or board[tmp_y][tmp_x] == chess['w_rook']
                                                 or board[tmp_y][tmp_x] == chess['w_knight']
                                                 or board[tmp_y][tmp_x] == chess['w_bishop']
                                                 or board[tmp_y][tmp_x] == chess['w_queen']):
                break

        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

        while 8 > tmp_x >= 0 and 8 > tmp_y >= 0:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

            elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                 or board[tmp_y][tmp_x] == chess['b_rook']
                                                 or board[tmp_y][tmp_x] == chess['b_knight']
                                                 or board[tmp_y][tmp_x] == chess['b_bishop']
                                                 or board[tmp_y][tmp_x] == chess['b_queen']
                                                 or board[tmp_y][tmp_x] == chess['w_pawn']
                                                 or board[tmp_y][tmp_x] == chess['w_rook']
                                                 or board[tmp_y][tmp_x] == chess['w_knight']
                                                 or board[tmp_y][tmp_x] == chess['w_bishop']
                                                 or board[tmp_y][tmp_x] == chess['w_queen']):

                break

        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

        while 8 > tmp_x >= 0:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

            elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                 or board[tmp_y][tmp_x] == chess['b_rook']
                                                 or board[tmp_y][tmp_x] == chess['b_knight']
                                                 or board[tmp_y][tmp_x] == chess['b_bishop']
                                                 or board[tmp_y][tmp_x] == chess['b_queen']
                                                 or board[tmp_y][tmp_x] == chess['w_pawn']
                                                 or board[tmp_y][tmp_x] == chess['w_rook']
                                                 or board[tmp_y][tmp_x] == chess['w_knight']
                                                 or board[tmp_y][tmp_x] == chess['w_bishop']
                                                 or board[tmp_y][tmp_x] == chess['w_queen']):
                break

        # Moving Left
        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

        while 0 <= tmp_x < 8:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

            elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                 or board[tmp_y][tmp_x] == chess['b_rook']
                                                 or board[tmp_y][tmp_x] == chess['b_knight']
                                                 or board[tmp_y][tmp_x] == chess['b_bishop']
                                                 or board[tmp_y][tmp_x] == chess['b_queen']
                                                 or board[tmp_y][tmp_x] == chess['w_pawn']
                                                 or board[tmp_y][tmp_x] == chess['w_rook']
                                                 or board[tmp_y][tmp_x] == chess['w_knight']
                                                 or board[tmp_y][tmp_x] == chess['w_bishop']
                                                 or board[tmp_y][tmp_x] == chess['w_queen']):
                break

        return possible_moves

    def __check(self, board, user, x, y):

        # From the current position of the chess piece
        # determine all possible paths and check if
        # at any point it attacks the king. If it down
        # return true else false

        # Checking right diagonal paths
        # Top
        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

        while tmp_x < 8 and tmp_y >= 0:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    break
            else:
                if board[tmp_y][tmp_x] == chess['b_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.right_diagnol_up(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']
                                                     or board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_king']):
                    break

        # Checking right diagonal paths
        # Bottom
        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

        while tmp_x < 8 and tmp_y < 8:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    break
            else:
                if board[tmp_y][tmp_x] == chess['b_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.right_diagnol_down(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']
                                                     or board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_king']):
                    break

        # Checking left diagonal paths
        # Top
        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

        while tmp_x >= 0 and tmp_y >= 0:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    break
            else:
                if board[tmp_y][tmp_x] == chess['b_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.left_diagnol_up(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']
                                                     or board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_king']):
                    break

        # Checking left diagonal paths
        # Bottom
        tmp_y = y
        tmp_x = x
        tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

        while tmp_x < 8 and tmp_y >= 0:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_king']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']):
                    break
            else:
                if board[tmp_y][tmp_x] == chess['b_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x, tmp_y = Movement.left_diagnol_down(tmp_x, tmp_y)

                elif board[tmp_y][tmp_x] != '0' and (board[tmp_y][tmp_x] == chess['w_pawn']
                                                     or board[tmp_y][tmp_x] == chess['w_rook']
                                                     or board[tmp_y][tmp_x] == chess['w_knight']
                                                     or board[tmp_y][tmp_x] == chess['w_bishop']
                                                     or board[tmp_y][tmp_x] == chess['w_queen']
                                                     or board[tmp_y][tmp_x] == chess['b_pawn']
                                                     or board[tmp_y][tmp_x] == chess['b_rook']
                                                     or board[tmp_y][tmp_x] == chess['b_knight']
                                                     or board[tmp_y][tmp_x] == chess['b_bishop']
                                                     or board[tmp_y][tmp_x] == chess['b_queen']
                                                     or board[tmp_y][tmp_x] == chess['w_king']):
                    break
        return False

    def ValidMove(self, board, user):

        # To check possible moves we will loop
        # our board
        legal = False
        attack = False
        check = False
        moves = Movement

        # 4 possible set of moves
        # Diagonally Right up and down
        # Diagonally Left up and down

        input_x = self.input_coordinates[1]
        input_y = self.input_coordinates[0]

        output_x = self.output_coordinates[1]
        output_y = self.output_coordinates[0]

        right_up = False
        right_down = False
        left_up = False
        left_down = False

        # Diagonally Right and Up
        # y value decreases x increases
        if output_x > input_x and output_y < input_y:
            right_up = True

        # Diagonally Right and Down
        # y value increases and x decreases
        elif output_x < input_x and output_y > input_y:
            right_down = True

        # Diagonally Left and Up
        # y value decreases and x decreases
        elif output_x < input_x and output_y < input_y:
            left_up = True

        # Diagonally Left and Down
        # y value increases and x increases
        elif output_x > input_x and output_y > input_y:
            left_down = True

        # Checking for legal moves
        if right_up:
            tmp_x = input_x
            tmp_y = input_y
            goal = False

            while not goal:
                tmp_x, tmp_y = moves.right_diagnol_up(tmp_x, tmp_y)

                # If goal reached check if our move attacks any opponent
                if output_x == tmp_x and output_y == tmp_y:
                    goal = True
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
                        break
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
                        break

                    # Check on board if the current move
                    # is legal
                if board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    legal = True
                else:
                    legal = False
                    break

        elif right_down:

            tmp_x = input_x
            tmp_y = input_y
            goal = False

            while not goal:
                tmp_x, tmp_y = moves.left_diagnol_down(tmp_x, tmp_y)

                # If goal reached check if our move attacks any opponent
                if output_x == tmp_x and output_y == tmp_y:
                    goal = True
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
                        break
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
                        break

                # Check on board if the current move
                # is legal
                if board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    legal = True
                else:
                    legal = False
                    break

        elif left_up:

            tmp_x = input_x
            tmp_y = input_y
            goal = False

            while not goal:
                tmp_x, tmp_y = moves.left_diagnol_up(tmp_x, tmp_y)

                # If goal reached check if our move attacks any opponent
                if output_x == tmp_x and output_y == tmp_y:
                    goal = True
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
                        break
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
                        break

                    # Check on board if the current move
                    # is legal
                if board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    legal = True
                else:
                    legal = False
                    break

        elif left_down:

            tmp_x = input_x
            tmp_y = input_y
            goal = False

            while not goal:
                tmp_x, tmp_y = moves.right_diagnol_down(tmp_x, tmp_y)

                # If goal reached check if our move attacks any opponent
                if output_x == tmp_x:
                    legal = True
                    goal = True

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
                        break
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
                        break

                # Check if the current move is legal
                if board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    legal = True
                else:
                    legal = False
                    break

        check_king = self.__check(board, user, output_x, output_y)
        if check_king:
            legal = True
            check = True
        return legal, attack, check
