def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive utility function to solve N-Queens problem
def solve_nqueens_util(board, col, n):
    # If all queens are placed, return True
    if col >= n:
        return True

    # Try placing a queen in all rows of this column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solve_nqueens_util(board, col + 1, n):
                return True

            # If placing queen at board[i][col] doesn't lead to a solution, remove it
            board[i][col] = 0  # Backtrack

    return False

# Function to initialize board with the first queen placed
def solve_nqueens(n, first_queen_row, first_queen_col):
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[first_queen_row][first_queen_col] = 1  # Place the first queen

    # Start solving from the next column
    if not solve_nqueens_util(board, first_queen_col + 1, n):
        print("Solution does not exist")
        return

    print("Final N-Queens Board:")
    print_board(board)

# Example usage
n = 8
first_queen_row = 0  # Row index for the first queen
first_queen_col = 0  # Column index for the first queen

solve_nqueens(n, first_queen_row, first_queen_col)
