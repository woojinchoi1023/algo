# https://www.acmicpc.net/problem/2239
import sys
sys.setrecursionlimit(10**6)
board = [list(map(int, input()))for _ in range(9)]
# 메모리 초과

rows = {
    i: set() for i in range(9)
}
cols = {
    i: set() for i in range(9)
}
blocks = {
    (i, j): set() for i in range(3) for j in range(3)
}


def block_check(r, c, num):
    if num in blocks[(r//3, c//3)]:
        return False
    return True


def row_check(r, c, num):
    if num in rows[r]:
        return False
    return True


def col_check(r, c, num):
    if num in cols[c]:
        return False
    return True


def dfs(idx):  # 왼쪽위부터 오른쪽으로 0 1 2 3.... 80
    if idx == 81:
        for x in range(9):
            print(''.join(map(str, board[x])))
        exit(0)
        return
    r = idx//9
    c = idx % 9
    if board[r][c] != 0:
        dfs(idx+1)
        return
    for i in range(1, 10):
        if block_check(r, c, i) and row_check(r, c, i) and col_check(r, c, i):
            board[r][c] = i
            blocks[(r//3, c//3)].add(i)
            rows[r].add(i)
            cols[c].add(i)
            dfs(idx+1)
            board[r][c] = 0
            blocks[(r//3, c//3)].remove(i)
            rows[r].remove(i)
            cols[c].remove(i)


for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            blocks[(i//3, j//3)].add(board[i][j])
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])

dfs(0)
