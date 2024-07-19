# https://www.acmicpc.net/problem/2239
import sys
# 시간초과
sys.setrecursionlimit(10**6)
board = [list(map(int, input()))for _ in range(9)]


def block_check(r, c, num):
    for row in range(r//3*3, r//3*3+3):
        for col in range(c//3*3, c//3*3+3):
            if board[row][col] == num:
                return False
    return True


def cross_check(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    return True


ans = []


def dfs(idx):  # 왼쪽위부터 오른쪽으로 0 1 2 3.... 80
    # print(idx)
    if idx == 81:
        for x in range(9):
            print(''.join(map(str, board[x])))
        # print(board)
        return
    r = idx//9
    c = idx % 9
    if board[r][c] != 0:
        dfs(idx+1)
        return
    for i in range(1, 10):
        if block_check(r, c, i) and cross_check(r, c, i):
            board[r][c] = i
            dfs(idx+1)
            board[r][c] = 0


dfs(0)
# print(*ans, sep='\n')
