# https://www.acmicpc.net/problem/2239
import sys
input = sys.stdin.readline
board = [list(map(int, input().rstrip('\n')))for _ in range(9)]

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


def dfs(idx):
    if idx == len(zeros):
        for x in range(9):
            print(''.join(map(str, board[x])))
        exit(0)
    r, c = zeros[idx]
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


zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            blocks[(i//3, j//3)].add(board[i][j])
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
        else:
            zeros.append((i, j))

dfs(0)
