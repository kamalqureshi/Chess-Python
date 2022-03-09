import Movement
from Movement import *
import numpy as np
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


class Pawn:
    abb = 'p'

    def __init__(self, color, input_coordinates, output_coordinates):
        self.color = color
        self.input_coordinates = input_coordinates
        self.output_coordinates = output_coordinates

    def ValidMove(self, board):
        possible_moves = []
        new_move = []
        legal_move = False
        check = False
        temp_input = self.input_coordinates
        if self.color == 'W' or self.color == 'w':
            if self.input_coordinates[0] == 6:  # if pawn can move two squares
                # to see if first square is empty

                if board[temp_input[0]-1][temp_input[1]] == chess['b_checker'] or \
                        board[temp_input[0]-1][temp_input[1]] == chess['w_checker'] or \
                        board[temp_input[0]-1][temp_input[1]] == '0':
                    legal_move = True
                    if legal_move:
                        new_move.append(temp_input[0]-1)
                        new_move.append(temp_input[1])
                        if new_move[0] < 8 and new_move[1] < 8 and new_move[0] >= 0 and new_move[1] >= 0:
                            possible_moves.append(new_move[:])
                            legal_move = False
                        legal_move = False
                        new_move.clear()

                        # TO SEE IF SECOND SQUARE IS EMPTY
                        if board[temp_input[0]-2][temp_input[1]] == chess['b_checker'] or \
                                board[temp_input[0]-2][temp_input[1]] == chess['w_checker'] or \
                                board[temp_input[0]-2][temp_input[1]] == '0':
                            legal_move = True
                            if legal_move:
                                new_move.append(temp_input[0] - 2)
                                new_move.append(temp_input[1])
                                if new_move[0] < 8 and new_move[1] < 8 and new_move[0] >= 0 and new_move[1] >= 0:
                                    possible_moves.append(new_move[:])
                                    legal_move = False
                                legal_move = False
                                new_move.clear()

            # NORMAL MOVEMENT
            else:
                if board[temp_input[0]-1][temp_input[1]] == chess['b_checker'] or \
                    board[temp_input[0]-1][temp_input[1]] == chess['w_checker'] \
                        or board[temp_input[0]-1][temp_input[1]] == '0':
                    legal_move = True
                    if legal_move:
                        new_move.append(temp_input[0]-1)
                        new_move.append(temp_input[1])
                        if new_move[0] < 8 and new_move[1] < 8 and new_move[0] >= 0 and new_move[1] >= 0:
                            possible_moves.append(new_move[:])
                            legal_move = False
                        legal_move = False
                        new_move.clear()

            # KILL CODE
            tmp = temp_input
            for i in range(1):
                kill1x, kill1y = Movement.right_diagnol_up(tmp[0], tmp[1])
                if (kill1x < 8 and kill1y < 8) and (kill1x >= 0 and kill1y >= 0):
                    if self.capture_pieces(kill1x, kill1y, board):
                        new_move.append(kill1x)
                        new_move.append(kill1y)
                        possible_moves.append(new_move[:])
                        new_move.clear()

                kill2x, kill2y = Movement.left_diagnol_up(tmp[0], tmp[1])
                if (kill2x < 8 and kill2y < 8) and (kill2x >= 0 and kill2y >= 0):
                    if self.capture_pieces(kill2x, kill2y, board):
                        new_move.append(kill2x)
                        new_move.append(kill2y)
                        possible_moves.append(new_move[:])
                        new_move.clear()



        # COLOR IS BLACK
        if self.color == 'B' or self.color == 'b':
            # MOVEMENT TO CHECK IF PAWN CAN MOVE TWO SQUARES
            if self.input_coordinates[0] == 1:
                # CHECK TO SEE FIRST SQUARE AS EMPTY
                if board[temp_input[0] + 1][temp_input[1]] == chess['b_checker'] or \
                        board[temp_input[0] + 1][temp_input[1]] == chess['w_checker'] or \
                        board[temp_input[0]+1][temp_input[1]] == '0':
                    legal_move = True
                    if legal_move:
                        new_move.append(temp_input[0] + 1)
                        new_move.append(temp_input[1])
                        if new_move[0] < 8 and new_move[1] < 8 and new_move[0] >= 0 and new_move[1] >= 0:
                            possible_moves.append(new_move[:])
                            legal_move = False
                        legal_move = False
                        new_move.clear()

                        # CHECK TO SEE IF SECOND SQUARE IS EMPTY
                        if board[temp_input[0] + 2][temp_input[1]] == chess['b_checker'] or \
                                board[temp_input[0] + 2][temp_input[1]] == chess['w_checker'] or \
                                board[temp_input[0]+2][temp_input[1]] == '0':
                            legal_move = True
                            if legal_move:
                                new_move.append(temp_input[0] + 2)
                                new_move.append(temp_input[1])
                                if new_move[0] < 8 and new_move[1] < 8 and new_move[0] >= 0 and new_move[1] >= 0:
                                    possible_moves.append(new_move[:])
                                    legal_move = False
                                legal_move = False
                                new_move.clear()

            # NORMAL MOVEMENT
            else:
                if board[temp_input[0] + 1][temp_input[1]] == chess['b_checker'] or \
                        board[temp_input[0] + 1][temp_input[1]] == chess['w_checker'] or \
                        board[temp_input[0]+1][temp_input[1]] == '0':
                    legal_move = True
                    if legal_move:
                        new_move.append(temp_input[0] + 1)
                        new_move.append(temp_input[1])
                        if new_move[0] < 8 and new_move[1] < 8 and new_move[0] >= 0 and new_move[1] >= 0:
                            possible_moves.append(new_move[:])
                            legal_move = False
                        legal_move = False
                        new_move.clear()

            # KILL CODE
            tmp = temp_input
            for i in range(1):
                kill1x, kill1y = Movement.right_diagnol_down(tmp[0], tmp[1])
                if (kill1x < 8 and kill1y < 8) and (kill1x >= 0 and kill1y >= 0):
                    if self.capture_pieces(kill1x, kill1y, board):
                        new_move.append(kill1x)
                        new_move.append(kill1y)
                        possible_moves.append(new_move[:])
                        new_move.clear()

                kill2x, kill2y = Movement.left_diagnol_down(tmp[0], tmp[1])
                if (kill2x < 8 and kill2y < 8) and (kill2x >= 0 and kill2y >= 0):
                    if self.capture_pieces(kill2x, kill2y, board):
                        new_move.append(kill2x)
                        new_move.append(kill2y)
                        possible_moves.append(new_move[:])
                        new_move.clear()

        # print(possible_moves)
        return possible_moves

    def validate_move(self, board):
        possible_moves = self.ValidMove(board)
        possible_moves = np.array(possible_moves)
        for i in range(len(possible_moves)):
            for j in range(len(possible_moves[i])):
                if self.output_coordinates[0] == possible_moves[i][j] and j != 1:
                    if self.output_coordinates[1] == possible_moves[i][j+1]:
                        return True
        return False

    def capture_pieces(self, x, y, board):
        c = self.color.lower()
        if board[x][y] == chess[c+'_pawn'] or board[x][y] == chess[c+'_bishop'] or board[x][y] == chess[c+'_rook']:
            return True
        return False

    def checkKing(self, x, y, board):
        c = self.color.lower()
        if board[x][y] == chess[c+'_king']:
            return True
        else:
            return False
