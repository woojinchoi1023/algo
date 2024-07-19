# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
ls = []
for i in range(N):
    ls.append(list(map(int, input().rstrip('\n').split())))
q = []
for i in range(M):
    q.append(list(map(int, input().rstrip('\n').split())))

print(ls)
print(q)
for i in range(N):
    for j in range(1, N):
        ls[i][j] += ls[i][j-1]
print(ls)
for a, b, c, d in q:
    ans = 0
    for row in range(a-1, c):
        temp = ls[row][b-2] if b-2 > -1 else 0
        ans += ls[row][d-1] - temp
    print(ans)
