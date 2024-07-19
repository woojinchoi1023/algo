import sys
sys.setrecursionlimit(10 ** 4)

N = int(input())

cnt = 0


def dfs(row: int, col: set, diag: set, antidiag: set):
    global N, cnt
    if row == N:
        cnt += 1
        return
    for c in range(N):
        if (c not in col) and (row-c not in diag) and (row+c not in antidiag):
            col.add(c)
            diag.add(row-c)
            antidiag.add(row+c)
            dfs(row+1, col, diag, antidiag)
            col.remove(c)
            diag.remove(row-c)
            antidiag.remove(row+c)


dfs(0, set(), set(), set())
print(cnt)
