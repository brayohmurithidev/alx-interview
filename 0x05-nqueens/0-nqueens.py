#!/usr/bin/python3
import sys

'''N QUEENS'''


def solve_nqueens(n):
    '''Solve Queens'''
    def is_safe(board, row, col):
        '''check if safe'''
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solve_util(board, col, solutions):
        '''Solve for utilities'''
        if col == n:
            solutions.append(board[:])
            return

        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                solve_util(board, col + 1, solutions)
                board[col] = -1

    board = [-1] * n
    solutions = []
    solve_util(board, 0, solutions)

    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_nqueens(n)
