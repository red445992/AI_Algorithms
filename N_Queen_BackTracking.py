# this is a solution of N-queen problem with using recursion ie. backtracking approach
def is_safe(board,row,col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True


def solve_n_queens_backtrack(N,board=[],row=0):
    if row == N :
        print(f"solution: {board}")
        return True
    for col in range(N):
        if is_safe(board,row,col):
            board.append(col)
            if solve_n_queens_backtrack(N,board,row+1):
                return True
            board.pop()
    return False


if __name__ == "__main__":
    x = int(input("Enter the number of rows: "))
    y = int(input("Enter the number of columns: "))
    print(f"Board size: {x} x {y}")

    solve_n_queens_backtrack(x)