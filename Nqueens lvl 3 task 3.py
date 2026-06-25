def print_board(board, N):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, N):

    # Left side row check
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Lower left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, N):

    if col >= N:
        return True

    for row in range(N):

        if is_safe(board, row, col, N):

            board[row][col] = 'Q'

            if solve_nqueens(board, col + 1, N):
                return True

            board[row][col] = '.'

    return False


def main():

    N = int(input("Enter value of N: "))

    board = [['.' for _ in range(N)] for _ in range(N)]

    if solve_nqueens(board, 0, N):

        print("\nSolution Found:\n")
        print_board(board, N)

    else:
        print("No Solution Exists")


main()