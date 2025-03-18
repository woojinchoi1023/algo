# https://www.acmicpc.net/problem/2239
import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip('\n')))for _ in range(9)]


def block_check(r, c, num):
    for row in range(r//3*3, r//3*3+3):
        for col in range(c//3*3, c//3*3+3):
            if board[row][col] == num:
                return False
    return True


def row_check(r, c, num):
    for i in range(9):
        if board[i][c] == num:
            return False
    return True


def col_check(r, c, num):
    for i in range(9):
        if board[r][i] == num:
            return False
    return True


zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))


def dfs(depth):
    if depth == len(zeros):
        for x in range(9):
            print(''.join(map(str, board[x])))
        exit()
    r, c = zeros[depth]
    for i in range(1, 10):
        if col_check(r, c, i) and row_check(r, c, i) and block_check(r, c, i):
            board[r][c] = i
            dfs(depth+1)
            board[r][c] = 0


dfs(0)
