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


class Rook:

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
        tmp_y = Movement.up(tmp_y)
        tmp_x = x

        while tmp_y >= 0:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_y = Movement.up(tmp_y)

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
        tmp_y = Movement.down(tmp_y)
        tmp_x = x

        while tmp_y < 8:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_y = Movement.down(tmp_y)

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
        tmp_x = Movement.right(tmp_x)


        while tmp_x < 8:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_x = Movement.right(tmp_x)

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
        tmp_x = Movement.left(tmp_x)

        while tmp_x >= 0:
            if board[tmp_y][tmp_x] == chess['w_king'] or board[tmp_y][tmp_x] == chess['b_king']:
                break

            elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                    or board[tmp_y][tmp_x] == chess['w_checker']:

                possible_moves.append([tmp_y, tmp_x])
                tmp_x = Movement.left(tmp_x)

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

        # Checking all Vertical Paths
        # Moving Upwards
        tmp_y = y
        tmp_y = Movement.up(tmp_y)
        tmp_x = x

        while tmp_y >= 0:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_y = Movement.up(tmp_y)

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
                    tmp_y = Movement.up(tmp_y)

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

        # Moving Downwards
        tmp_y = y
        tmp_y = Movement.down(tmp_y)
        tmp_x = x

        while tmp_y < 8:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_y = Movement.down(tmp_y)

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
                    tmp_y = Movement.down(tmp_y)

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

        # Horizontal Movement
        # Moving Right
        tmp_y = y
        tmp_x = x
        tmp_x = Movement.right(tmp_x)

        while tmp_x < 8:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x = Movement.right(tmp_x)

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
                    tmp_y = Movement.up(tmp_y)

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

        # Moving Left
        tmp_y = y
        tmp_x = x
        tmp_x = Movement.left(tmp_x)

        while tmp_x >= 0:
            if user == 'W':
                if board[tmp_y][tmp_x] == chess['w_king']:
                    return True

                elif board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    tmp_x = Movement.left(tmp_x)

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
                    tmp_y = Movement.up(tmp_y)

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

        # For vertical or horizontal move we first check
        # if one of the coordinate is constant. If not then
        # it is not a valid move
        input_x = self.input_coordinates[1]
        input_y = self.input_coordinates[0]

        output_x = self.output_coordinates[1]
        output_y = self.output_coordinates[0]

        move_horizontal = False
        move_vertical = False

        print(input_x, input_y, output_x, output_y)

        if input_x == output_x or input_y == output_y:
            legal = True

            # Identify where our rookie will move
            if output_y == input_y:
                move_horizontal = True
            if output_x == input_x:
                move_vertical = True

            # If output at same position then invalid move
            if move_horizontal and move_vertical:
                legal = False

        if not legal:
            return legal, attack, check

        # With this variable we first checked if
        # movement was possible altogether
        # If we can actually move the piece
        # This variable will be True
        legal = False

        # Check if the piece can be moved
        # to the coordinates
        # Y Axis ( [1] )
        if move_horizontal:

            tmp_x = input_x
            tmp_y = input_y
            goal = False

            # Moving horizontally right
            # x axis increases
            while output_x > tmp_x and not goal:
                tmp_x = moves.right(tmp_x)

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
                            if board[tmp_y][tmp_x] == chess['w_king']:
                                legal = False
                                attack = False
                                check = True
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
                            if board[tmp_y][tmp_x] == chess['b_king']:
                                legal = False
                                attack = False
                                check = True
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

            # Moving horizontally left
            # x axis decrease
            while output_x < tmp_x and not goal:
                tmp_x = moves.left(tmp_x)

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
                            if board[tmp_y][tmp_x] == chess['w_king']:
                                legal = False
                                attack = False
                                check = True
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
                            if board[tmp_y][tmp_x] == chess['b_king']:
                                legal = False
                                attack = False
                                check = True
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

            check_king = self.__check(board, user, tmp_x, tmp_y)
            if check_king:
                legal = True
                check = True

            return legal, attack, check

        # Moving Vertically
        elif move_vertical:

            tmp_x = input_x
            tmp_y = input_y
            goal = False

            # Moving Vertically Down
            # y axis increases
            while output_y > tmp_y and not goal:
                tmp_y = moves.down(tmp_y)

                # If goal reached check if our move attacks any opponent
                if output_y == tmp_y:
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
                            if board[tmp_y][tmp_x] == chess['w_king']:
                                legal = False
                                attack = False
                                check = True
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
                            if board[tmp_y][tmp_x] == chess['b_king']:
                                legal = False
                                attack = False
                                check = True
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

            # Moving Vertically Up
            # y axis decrease
            while output_y < tmp_y and not goal:
                tmp_y = moves.up(tmp_y)

                # If goal reached check if our move attacks any opponent
                if output_y == tmp_y:
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
                            if board[tmp_y][tmp_x] == chess['w_king']:
                                legal = False
                                attack = False
                                check = True
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
                            if board[tmp_y][tmp_x] == chess['b_king']:
                                legal = False
                                attack = False
                                check = True
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
                print(board[tmp_y][tmp_x])
                print(u'\u25FB')
                print(u'\u25FC')
                if board[tmp_y][tmp_x] == '0' or board[tmp_y][tmp_x] == chess['b_checker'] \
                        or board[tmp_y][tmp_x] == chess['w_checker']:
                    legal = True
                else:
                    legal = False
                    break

            check_king = self.__check(board, user, tmp_x, tmp_y)
            if check_king:
                legal = True
                check = True

            return legal, attack, check

        # print("Board printed from Rook\n")
        # print(board)
        return legal, attack, check
