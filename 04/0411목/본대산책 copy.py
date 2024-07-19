# https://www.acmicpc.net/problem/14289
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = [[0]*N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    ls[x-1][y-1] = 1
    ls[y-1][x-1] = 1

temp = [0]*N
temp[0] = 1

D = int(input())


def product(res):
    new_temp = [0]*N
    for i in range(N):
        for j in range(N):
            new_temp[i] += res[i][j] * temp[j]
    return new_temp


def cal(arr1, arr2):
    new_ls = [[0]*N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                new_ls[k][i] += arr1[k][j] * arr2[j][i]
            new_ls[k][i] %= 1000000007
    return new_ls


ans = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            ans[i][j] = 1

while D:
    if D % 2:
        ans = cal(ans, ls)
    ls = cal(ls, ls)
    D //= 2

print(product(ans)[0])
