import math

def evaluate(board):
    win_combination = [
        [0,1,2],[3,4,5],[6,7,8],
        [1,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]    
    ]

    for comb in win_combination:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != " ":
            return 10 if board[0] == "X" else -10
    return 0

def is_move_left(board):
    return " " in board


def minmax(board,depth,alpha,beta,is_maximizer):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score
    if not is_move_left(board):
        return 0
    
    if is_maximizer:
        best = -math.inf

        for move in possible_moves(board):
            make_move(board,move,"X")

            best = max(best,minmax(board,depth+1,alpha,beta,False))

            undo_move(board,move)

            alpha = max(alpha,best)

            if beta <= alpha:
                break
        return best
    else:
        best = math.inf

        for move in possible_moves(board):
            make_move(board,move,"O")
            best = min(best,minmax(board,depth+1,alpha,beta,True))
            undo_move(board,move)

            beta = min(beta,best)

            if alpha<=beta:
                break
        return best
    
def find_best_move(board):
    best_val = -math.inf
    best_move = None

    for move in possible_moves(board):
        make_move(board,move,"X")
        move_val = minmax(board,0,-math.inf,math.inf,False)
        undo_move(board,move)

        if move_val > best_val:
            best_move = move
            best_val = move_val
    return best_move

def possible_moves(board):
    return [i for i in range(len(board)) if board[i] == " "]

def make_move(board, move, player):
    board[move] = player

def undo_move(board, move):
    board[move] = " "

if __name__ == "__main__":
    # Initial board configuration
    board = [
        "X", "O", "X",
        "O", " ", "O",
        " ", " ", " "
    ]
    
    best_move = find_best_move(board)
    print(f"The best move for 'X' is at position: {best_move}")