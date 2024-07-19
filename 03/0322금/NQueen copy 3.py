# https://www.acmicpc.net/problem/9663
import sys
sys.setrecursionlimit(10 ** 4)

N = int(input())

cnt = 0
col = [0] * (N*2+1)
diag = [0] * (N*2+1)
antidiag = [0] * (N*2+1)


def dfs(row):
    global N, cnt
    if row == N:
        cnt += 1
        return
    for c in range(N):
        if (col[c] == 0) and (diag[row-c] == 0) and (antidiag[row+c] == 0):
            col[c] = 1
            diag[row-c] = 1
            antidiag[row+c] = 1
            dfs(row+1)
            col[c] = 0
            diag[row-c] = 0
            antidiag[row+c] = 0


dfs(0)
print(cnt)
