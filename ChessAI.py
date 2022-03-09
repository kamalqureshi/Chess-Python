import Bishop
import King
import Knight
import Pawn
import random
import numpy as np
import copy
import Queen
import Rook

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


def getchecks():
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


def board_state_change(temp_board, board, temp_input, temp_output):
    temp_piece = board[temp_input[0]][temp_input[1]]
    board[temp_input[0]][temp_input[1]] = temp_board[temp_input[0]][temp_input[1]]
    board[temp_output[0]][temp_output[1]] = temp_piece
    return board


class Bot:
    piece_score = {'q': 9, 'k': 0, 'n': 3, 'r': 5, 'p': 1, 'b': 3}
    mate = 500

    def __init__(self, color, board):
        self.color = color
        self.board = board

    def generatemove(self, board):
        c = self.color.lower()
        moves = []
        temp_input = []

        # AI IS PLAYING BLACK COLOR
        if c == 'b':
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == chess['w_pawn']:
                        temp_input.append(i)
                        temp_input.append(j)
                        p = Pawn.Pawn(c, temp_input, 0)
                        possible_moves = p.ValidMove(board)
                        for l in range(len(possible_moves)):
                            for m in range(len(possible_moves[l])):
                                if m == 0:
                                    temp_output = list()
                                    temp_output.append(possible_moves[l][m])
                                    temp_output.append(possible_moves[l][m + 1])
                                    moves.append([temp_input[:], temp_output[:], 'p'])
                        possible_moves.clear()

                    elif board[i][j] == chess['w_rook']:
                        temp_input.append(i)
                        temp_input.append(j)
                        rook_obj = Rook.Rook()
                        possible_moves = rook_obj.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'r'])
                        possible_moves.clear()

                    elif board[i][j] == chess['w_bishop']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_bishop = Bishop.Bishop()
                        possible_moves = obj_bishop.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'b'])
                        possible_moves.clear()

                    elif board[i][j] == chess['w_queen']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_queen = Queen.Queen()
                        possible_moves = obj_queen.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'q'])
                        possible_moves.clear()

                    elif board[i][j] == chess['w_knight']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_knight = Knight.Knight()
                        possible_moves = obj_knight.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'k'])
                        possible_moves.clear()

                    elif board[i][j] == chess['w_king']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_king = King.King()
                        possible_moves = obj_king.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'kn'])
                        possible_moves.clear()

                    temp_input.clear()

            count = random.randint(0, len(moves))
            for i in range(len(moves)):
                for j in range(len(moves[i])):
                    if i == count and j == 0:
                        return moves[i][j], moves[i][j + 1], moves[i][j + 2]

        # AI IS PLAYING WHITE COLOR
        elif c == 'w':
            for i in range(len(board)):
                for j in range(len(board[i])):

                    if board[i][j] == chess['b_pawn']:
                        temp_input.append(i)
                        temp_input.append(j)
                        p = Pawn.Pawn(c, temp_input, 0)
                        possible_moves = p.ValidMove(board)
                        for l in range(len(possible_moves)):
                            for m in range(len(possible_moves[l])):
                                if m == 0:
                                    temp_output = list()
                                    temp_output.append(possible_moves[l][m])
                                    temp_output.append(possible_moves[l][m + 1])
                                    moves.append([temp_input[:], temp_output[:], 'p'])
                        possible_moves.clear()

                    elif board[i][j] == chess['b_rook']:
                        temp_input.append(i)
                        temp_input.append(j)
                        rook_obj = Rook.Rook()
                        possible_moves = rook_obj.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'r'])
                        possible_moves.clear()

                    elif board[i][j] == chess['b_bishop']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_bishop = Bishop.Bishop()
                        possible_moves = obj_bishop.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'b'])
                        possible_moves.clear()

                    elif board[i][j] == chess['b_queen']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_queen = Queen.Queen()
                        possible_moves = obj_queen.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'q'])
                        possible_moves.clear()

                    elif board[i][j] == chess['b_knight']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_knight = Knight.Knight()
                        possible_moves = obj_knight.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'k'])
                        possible_moves.clear()

                    elif board[i][j] == chess['b_king']:
                        temp_input.append(i)
                        temp_input.append(j)
                        obj_king = King.King()
                        possible_moves = obj_king.possibleMoves(board, c, i, j)
                        print(possible_moves)
                        if possible_moves is not None:
                            for l in range(len(possible_moves)):
                                for m in range(len(possible_moves[l])):
                                    if m == 0:
                                        temp_output = list()
                                        temp_output.append(possible_moves[l][m])
                                        temp_output.append(possible_moves[l][m + 1])
                                        moves.append([temp_input[:], temp_output[:], 'kn'])
                        possible_moves.clear()

                    temp_input.clear()
        return moves

    def scorePiece(self, board):
        score = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.color == 'W':
                    if board[i][j] == chess['b_pawn']:
                        score += self.piece_score['p']
                    elif board[i][j] == chess['b_rook']:
                        score += self.piece_score['r']
                    elif board[i][j] == chess['b_bishop']:
                        score += self.piece_score['b']
                    elif board[i][j] == chess['b_knight']:
                        score += self.piece_score['n']
                    elif board[i][j] == chess['b_queen']:
                        score += self.piece_score['q']

                elif self.color == 'B':
                    if board[i][j] == chess['w_pawn']:
                        score -= self.piece_score['p']
                    elif board[i][j] == chess['w_rook']:
                        score -= self.piece_score['r']
                    elif board[i][j] == chess['w_bishop']:
                        score -= self.piece_score['b']
                    elif board[i][j] == chess['w_knight']:
                        score -= self.piece_score['n']
                    elif board[i][j] == chess['w_queen']:
                        score -= self.piece_score['q']
        return score

    def score_calculate_white(self, board):
        score = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == chess['b_pawn']:
                    score += self.piece_score['p']
                elif board[i][j] == chess['b_rook']:
                    score += self.piece_score['r']
                elif board[i][j] == chess['b_bishop']:
                    score += self.piece_score['b']
                elif board[i][j] == chess['b_knight']:
                    score += self.piece_score['n']
                elif board[i][j] == chess['b_queen']:
                    score += self.piece_score['q']
        return score

    def score_calculate_black(self, board):
        score = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == chess['w_pawn']:
                    score += self.piece_score['p']
                elif board[i][j] == chess['w_rook']:
                    score += self.piece_score['r']
                elif board[i][j] == chess['w_bishop']:
                    score += self.piece_score['b']
                elif board[i][j] == chess['w_knight']:
                    score += self.piece_score['n']
                elif board[i][j] == chess['w_queen']:
                    score += self.piece_score['q']
        return score

    def findBestMove(self):
        # WHEN AI IS BLACK, WE FIND THE MAX BEST SCORE FOR BLACK WHILE WHITE SCORE IS MIN
        if self.color == 'B':
            moves = self.generatemove(self.board)  # input, output
            temp_board1 = copy.deepcopy(self.board)
            tmp = getchecks()
            best_black_score = -999
            best_white_score = 999
            black_score = []
            white_score = []
            moves_white = self.generatemove(self.board)
            k = 0
            # CALCULATING SCORES
            for i in range(len(moves)):
                new_board = board_state_change(tmp, temp_board1, moves[i][k], moves[i][k + 1])
                score = self.scorePiece(new_board)
                white_score.append(self.score_calculate_white(new_board))
                black_score.append(int(score))

            # FINDING MAX BEST SCORE FOR BLACK AND MIN BEST SCORE FOR WHITE
            for i in range(len(black_score)):
                if black_score[i] > best_black_score:
                    best_score = black_score[i]
                if white_score[i] < best_white_score:
                    best_white_score = white_score[i]

            # SHUFFLING THE ARRAY
            random.shuffle(moves)
            # FINDING THE MOVE WHERE BLACK HAS MAX SCORE AND WHITE HAS MIN SCORE
            for i in range(len(moves)):
                original_board = copy.deepcopy(self.board)
                new_board = board_state_change(tmp, original_board, moves[i][k], moves[i][k + 1])
                score = self.scorePiece(new_board)
                score_w = self.score_calculate_white(new_board)
                if best_score == score and score_w == best_white_score:
                    return moves[i][k], moves[i][k + 1], moves[i][k + 2]
