# https://www.acmicpc.net/problem/2239
import sys
sys.setrecursionlimit(10**6)
board = [list(map(int, input()))for _ in range(9)]


def block_check(r, c, num):
    for row in range(r//3, r//3+3):
        for col in range(c//3, c//3+3):
            if board[row][col] == num:
                return False
    return True


def cross_check(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    return True


print(*board, sep='\n')
