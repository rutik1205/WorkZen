
N = 9

# Check whether a queen can be placed
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        elif board[i]-i == col-row:
            return False
        elif board[i]+i == col+row:
            return False
    return True

def solve_queens(board, row):

    if row == N:
        return True

    for col in range(N):
        if is_safe(board,row,col):
            board[row] = col
            if solve_queens(board,row+1):
                return True
            # Remove queen (Backtrack)
            board[row] = -1

    return False

board = [-1] * N

if solve_queens(board, 0):
    print("Solution found:")
    print()

    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution found.")
