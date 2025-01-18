
# let us consider the 4x4 chess board
# this is a solution of N-queen problem with out using recursion ie. iterative approach

def is_safe(board,row,col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True


def solve_n_queens_iterative(N):
    stack = []
    row = 0
    board = [-1] * N

    while row<N:
        placed = False
        for col in range(board[row]+1,N):
            if is_safe(board,row,col):
                board[row] = col
                stack.append((row,col))
                placed = True
                break
        if not placed:
            if not stack:
                print("no solution found!")
                return
            row,col = stack.pop()
            board[row] = -1
            row -= 1
        else:
            row += 1 
    print(f"solution:{board}")


if __name__ == "__main__":
    x = int(input("Enter the number of rows: "))
    y = int(input("Enter the number of columns: "))
    print(f"Board size: {x} x {y}")

    solve_n_queens_iterative(x)