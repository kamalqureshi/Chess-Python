import numpy as np
import Movement
import Pawn
import ChessAI
import time
import King
import Queen
import Rook as rookie
import Bishop as bish
import Knight as knight

# DICTIONARY TO MAP UNICODE OBJECTS
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


# FUNCTION TO PRINT CHECKERS WITHOUT ANY PIECE ON BOARD
def getchecks(user):
    bw_row = [chess['b_checker'], chess['w_checker']] * 4
    # print(bw_row)
    bw_checkers = []

    for i in range(8):
        bw_checkers.append(bw_row if i % 2 == 0 else bw_row[::-1])
    # print(bw_checkers)
    bw_checkers = np.array(bw_checkers)
    # print(bw_checkers)
    wb_checkers = bw_checkers[::-1]
    # print(wb_checkers)
    board = []
    for _ in range(4):
        board.append(['0'] * 8)

    return wb_checkers


# FUNCTION TO PRINT CHEKCERS
def get_checkers():
    bw_row = [chess['b_checker'], chess['w_checker']] * 4
    # print(bw_row)
    bw_checkers = []

    for i in range(8):
        bw_checkers.append(bw_row if i % 2 == 0 else bw_row[::-1])
    # print(bw_checkers)
    bw_checkers = np.array(bw_checkers)
    # print(bw_checkers)
    wb_checkers = bw_checkers[::-1]
    # print(wb_checkers)
    return {'W': wb_checkers, 'B': bw_checkers}


# FUNCTION TO GET BOARD
def get_board():
    def get_army(user):
        u = user.lower()
        guard = [chess[u + '_rook'], chess[u + '_knight'], chess[u + '_bishop']]
        rear = guard + [chess[u + '_queen'], chess[u + '_king']] + guard[::-1]
        front = [chess[u + '_pawn']] * 8
        # print(front)
        if user == 'W':
            return [rear, front]
        else:
            return [front, rear]

    board = []
    board += get_army('W')
    # board = [squad for squad in get_army('B')]
    # board=[]
    for _ in range(4):
        board.append(['0'] * 8)
    # board += get_army('B')
    board += get_army('B')
    return np.array(board)


# FUNCTION TO PRINT BOARD
def print_board(board, checkers, user):
    count = 8
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    chks = checkers[user]
    temp = board.copy()  # if user == 'W' else board.copy()[::-1]
    for i, row in enumerate(temp):
        for j, c in enumerate(row):
            if c == '0':
                print('', chks[i][j], end='')
            else:
                print('', temp[i][j], end='')
        print(' ', count)
        count -= 1
    # print('')
    print('', *alphabets)
    # print(i, j)
    # time.sleep(5)
    # print('', chks[i][j] if c == '0' else c, end='', flush = True)


def board_state_change(temp_board, board, temp_input, temp_output):
    temp_piece = board[temp_input[0]][temp_input[1]]
    board[temp_input[0]][temp_input[1]] = temp_board[temp_input[0]][temp_input[1]]
    board[temp_output[0]][temp_output[1]] = temp_piece
    return board


def check_legal_move(board, temp_input):
    temp_piece = board[temp_input[0]][temp_input[1]]
    if temp_piece == chess['b_checker'] or temp_piece == chess['w_checker']:
        return True
    return False


# MAIN
if __name__ == "__main__":
    checkers = get_checkers()
    print("WELCOME TO CHESS")
    print("Select a color you want to play")
    print("for White, press W, \n", "for Black, press B, \n")
    user = input("enter the color you want to play: ")
    while user != 'W' and user != 'B':
        print("invalid input, enter again: ")
        user = input("enter the color you want to play: ")
    board = get_board()
    print_board(board, checkers, user)
    # with only checkers
    temp_board = getchecks(user)
    running = True
    PlayerOne = True
    PlayerTwo = True
    check = False
    check_mate = False
    if user == 'W':
        PlayerOne = True
        PlayerTwo = False
        turn = PlayerOne
        AI = 'B'
    else:
        PlayerOne = False
        PlayerTwo = True
        turn = PlayerTwo
        AI = 'W'
    print("GAME IS STARTING", '\n')
    if PlayerOne:
        while running:
            time.sleep(1)
            # USER HAS THE FIRST MOVE
            if turn == PlayerOne:
                print("IT IS YOUR TURN")
                print("enter p for pawn, b for bishop, q for queen, k for king, r for rook, kn for king")
                piece = input("enter the piece you want to move: ")
                while piece != "p" and piece != "b" and piece != "q" and piece != "k" and piece != "r" and piece != "kn":
                    print("INVALID INPUT, ENTER AGAIN:")
                    piece = input("enter the piece you want to move: ")
                if piece == "r":
                    obj_rook = rookie.Rook()
                elif piece == "b":
                    obj_bishop = bish.Bishop()
                elif piece == 'k':
                    obj_knight = knight.Knight()
                elif piece == 'kn':
                    obj_king = King.King()
                elif piece == 'q':
                    obj_queen = Queen.Queen()
                # INPUT COORDINATES
                print("enter current coordinates of selected piece: ")
                input_coordinates = list()
                x = int(input("enter row: "))
                while x < 1 or x > 8:
                    print("invalid input, enter again, A NUMBER BETWEEEN 1-8")
                    x = int(input("enter row: "))
                y = input("enter column: ")
                while y < 'a' or y > 'h':
                    print("invalid input, enter again, AN ALPHABET BETWEEEN A-G")
                    y = input("enter column: ")
                input_coordinates.append(x)
                input_coordinates.append(y)

                # OUTPUT COORDINATES
                output_coordinates = list()
                print("enter output coordinates")
                x = int(input("enter row: "))
                while x < 1 or x > 8:
                    print("invalid input, enter again, A NUMBER BETWEEEN 1-8")
                    x = int(input("enter row: "))
                y = input("enter column: ")
                while y < 'a' or y > 'h':
                    print("invalid input, enter again, AN ALPHABET BETWEEEN A-G")
                    y = input("enter column: ")
                output_coordinates.append(x)
                output_coordinates.append(y)

                # call to move class constructor
                M = Movement.Move(input_coordinates, output_coordinates)
                # converting coordinates to iteratables form
                temp_input = M.moving_input_coordinates()
                temp_output = M.moving_output_coordinates()

                # to make sure that input coordinates do not contain checkers
                while check_legal_move(board, temp_input):
                    print("THIS IS AN INVALID MOVE")
                    print("enter current coordinates of selected piece: ")
                    input_coordinates = list()
                    x = int(input("enter row: "))
                    y = input("enter column: ")
                    input_coordinates.append(x)
                    input_coordinates.append(y)

                    output_coordinates = list()
                    print("enter new coordinates")
                    x = int(input("enter row: "))
                    y = input("enter column: ")
                    output_coordinates.append(x)
                    output_coordinates.append(y)

                    # call to move class constructor
                    M = Movement.Move(input_coordinates, output_coordinates)
                    # converting coordinates to iteratables form
                    temp_input = M.moving_input_coordinates()
                    temp_output = M.moving_output_coordinates()

                # new board printed after changing of pieces

                print('\n')
                if piece == "r":
                    obj_rook.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_rook.ValidMove(board, user)

                elif piece == "b":
                    obj_bishop.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_bishop.ValidMove(board, user)

                elif piece == "k":
                    obj_knight.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_knight.ValidMove(board, user)

                elif piece == 'p':
                    p = Pawn.Pawn(user, temp_input, temp_output)
                    legal = p.validate_move(board)

                elif piece == "kn":
                    obj_king.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_king.ValidMove(board, user)

                elif piece == "q":
                    obj_queen.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_queen.ValidMove(board, user)
                if legal:
                    # new board printed after changing of pieces
                    if piece == 'p':
                        print("Pawn", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'b':
                        print("Bishop", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'q':
                        print("Queen", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'k':
                        print("Knight", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'kn':
                        print("King", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'r':
                        print("Rook", output_coordinates[0], output_coordinates[1], '\n')

                    new_board = board_state_change(temp_board, board, temp_input, temp_output)
                    print_board(new_board, checkers, user)
                    turn = PlayerTwo

                else:
                    print("\nInvalid Move\n")
                    temp_output = temp_input

            if turn == PlayerTwo:
                # ENTER AI GENERATION CODE
                print("HI, I AM AI, IT IS MY TURN", '\n')
                bot = ChessAI.Bot(AI, board)
                temp_input, temp_output, piece = bot.generatemove(board)
                new_board = board_state_change(temp_board, board, temp_input, temp_output)
                print_board(new_board, checkers, user)
                m = Movement.Move(temp_input, temp_output)
                output_coordinates = m.covert_output_coordinates(temp_output)
                if piece == 'p':
                    print("Pawn", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'b':
                    print("Bishop", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'q':
                    print("Queen", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'k':
                    print("Knight", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'kn':
                    print("King", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'r':
                    print("Rook", output_coordinates[0], output_coordinates[1], '\n')
                turn = PlayerOne
            time.sleep(1)

    elif not PlayerOne:
        while running:
            if turn == PlayerTwo:
                # ENTER AI GENERATION CODE
                print("HI, I AM AI, IT IS MY TURN", '\n')
                bot = ChessAI.Bot(AI, board)
                temp_input, temp_output, piece = bot.generatemove(board)
                new_board = board_state_change(temp_board, board, temp_input, temp_output)
                print_board(new_board, checkers, user)
                m = Movement.Move(temp_input, temp_output)
                output_coordinates = m.covert_output_coordinates(temp_output)
                if piece == 'p':
                    print("Pawn", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'b':
                    print("Bishop", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'q':
                    print("Queen", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'k':
                    print("Knight", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'kn':
                    print("King", output_coordinates[0], output_coordinates[1], '\n')

                elif piece == 'r':
                    print("Rook", output_coordinates[0], output_coordinates[1], '\n')
                turn = PlayerOne
            time.sleep(1)

            # USER HAS THE FIRST MOVE
            if turn == PlayerOne:
                print("IT IS YOUR TURN")
                print("enter p for pawn, b for bishop, q for queen, k for king, r for rook, kn for king")
                piece = input("enter the piece you want to move: ")
                while piece != "p" and piece != "b" and piece != "q" and piece != "k" and piece != "r" and piece != "kn":
                    print("INVALID INPUT, ENTER AGAIN:")
                    piece = input("enter the piece you want to move: ")
                if piece == "r":
                    obj_rook = rookie.Rook()
                elif piece == "b":
                    obj_bishop = bish.Bishop()
                elif piece == 'k':
                    obj_knight = knight.Knight()
                elif piece == 'kn':
                    obj_king = King.King()
                elif piece == 'q':
                    obj_queen = Queen.Queen()
                # INPUT COORDINATES
                print("enter current coordinates of selected piece: ")
                input_coordinates = list()
                x = int(input("enter row: "))
                while x < 1 or x > 8:
                    print("invalid input, enter again, A NUMBER BETWEEEN 1-8")
                    x = int(input("enter row: "))
                y = input("enter column: ")
                while y < 'a' or y > 'h':
                    print("invalid input, enter again, AN ALPHABET BETWEEEN A-G")
                    y = input("enter column: ")
                input_coordinates.append(x)
                input_coordinates.append(y)

                # OUTPUT COORDINATES
                output_coordinates = list()
                print("enter output coordinates")
                x = int(input("enter row: "))
                while x < 1 or x > 8:
                    print("invalid input, enter again, A NUMBER BETWEEEN 1-8")
                    x = int(input("enter row: "))
                y = input("enter column: ")
                while y < 'a' or y > 'h':
                    print("invalid input, enter again, AN ALPHABET BETWEEEN A-G")
                    y = input("enter column: ")
                output_coordinates.append(x)
                output_coordinates.append(y)

                # call to move class constructor
                M = Movement.Move(input_coordinates, output_coordinates)
                # converting coordinates to iteratables form
                temp_input = M.moving_input_coordinates()
                temp_output = M.moving_output_coordinates()

                # to make sure that input coordinates do not contain checkers
                while check_legal_move(board, temp_input):
                    print("THIS IS AN INVALID MOVE")
                    print("enter current coordinates of selected piece: ")
                    input_coordinates = list()
                    x = int(input("enter row: "))
                    y = input("enter column: ")
                    input_coordinates.append(x)
                    input_coordinates.append(y)

                    output_coordinates = list()
                    print("enter new coordinates")
                    x = int(input("enter row: "))
                    y = input("enter column: ")
                    output_coordinates.append(x)
                    output_coordinates.append(y)

                    # call to move class constructor
                    M = Movement.Move(input_coordinates, output_coordinates)
                    # converting coordinates to iteratables form
                    temp_input = M.moving_input_coordinates()
                    temp_output = M.moving_output_coordinates()

                # new board printed after changing of pieces

                print('\n')
                if piece == "r":
                    obj_rook.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_rook.ValidMove(board, user)

                elif piece == "b":
                    obj_bishop.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_bishop.ValidMove(board, user)

                elif piece == "k":
                    obj_knight.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_knight.ValidMove(board, user)

                elif piece == 'p':
                    p = Pawn.Pawn(user, temp_input, temp_output)
                    legal = p.validate_move(board)

                elif piece == "kn":
                    obj_king.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_king.ValidMove(board, user)

                elif piece == "q":
                    obj_queen.setCoordinates(temp_input, temp_output)
                    legal, attack, check = obj_queen.ValidMove(board, user)

                if legal:
                    # new board printed after changing of pieces
                    if piece == 'p':
                        print("Pawn", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'b':
                        print("Bishop", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'q':
                        print("Queen", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'k':
                        print("Knight", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'kn':
                        print("King", output_coordinates[0], output_coordinates[1], '\n')
                    elif piece == 'r':
                        print("Rook", output_coordinates[0], output_coordinates[1], '\n')

                    new_board = board_state_change(temp_board, board, temp_input, temp_output)
                    print_board(new_board, checkers, user)
                    turn = PlayerTwo
                else:
                    print("\nInvalid Move\n")
                    temp_output = temp_input


