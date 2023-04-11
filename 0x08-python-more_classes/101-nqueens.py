#!/usr/bin/python3
# 101-nqueens.py
"""This module contains a program that solves the N queens puzzle"""


def solve(board, col):
    """Utility function to solve the NQueens puzzle."""
    if col == N:
        tmp = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 1:
                    tmp.append([r, c])
        result.append(tmp)

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            solve(board, col + 1)

            board[i][col] = 0


def isSafe(board, x, y):
    """Verifies that a position (x, y) on the board is safe to place a Queen."""
    for i in range(y):
        if board[x][i] == 1:
            return False

    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(x, N, 1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def main():
    board = [[0 for i in range(N)] for i in range(N)]

    solve(board, 0)

    for r in result:
        print(r)


if __name__ == "__main__":
    import sys

    result = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    for c in sys.argv[1]:
        if ord(c) < 48 or ord(c) > 57:
            print("N must be a number")
            sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    main()
