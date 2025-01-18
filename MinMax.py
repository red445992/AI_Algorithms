import math
def evaluate(board):
    win_combination = [
        [0,1,2],[3,4,5],[6,7,8],
        [1,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]    
    ]

    for comb in win_combination:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != " ":
            return 10 if board[0]== "X" else -10
    return 0

def is_moves_left(board):
    return " " in board

# Minimax function
def minimax(board, depth, is_maximizer):
    score = evaluate(board)
    
    # If maximizer has won the game, return evaluated score
    if score == 10:
        return score - depth  # Prefer winning sooner
    
    # If minimizer has won the game, return evaluated score
    if score == -10:
        return score + depth  # Prefer losing later
    
    # If no more moves and no winner, it's a tie
    if not is_moves_left(board):
        return 0
    
    if is_maximizer:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, depth + 1, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, depth + 1, True))
                board[i] = " "
        return best

# Function to find the best move for the maximizer
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            move_val = minimax(board, 0, False)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# Example usage
if __name__ == "__main__":
    # Initial board configuration
    board = [
        "X", "O", "X",
        "O", "X", "O",
        " ", " ", " "
    ]
    
    best_move = find_best_move(board)
    print(f"The best move for 'X' is at position: {best_move}")
