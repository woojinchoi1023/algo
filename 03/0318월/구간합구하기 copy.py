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

temp = [
    (1, -1, 0),
    (1, 0, -1),
    (-1, -1, -1),
]
for i in range(N):
    for j in range(N):
        cand = [(a, b, c) for a, b, c in temp if -1 < j+c and -1 < i+b]
        for a, b, c in cand:
            ls[i][j] += a*ls[i+b][j+c]
# print(*ls, sep='\n')

for a, b, c, d in q:
    cand = [(z, x, y) for z, x, y in [(-1, c-1, b-2),
                                      (-1, a-2, d-1), (1, a-2, b-2)] if x > -1 and y > -1]
    ans = ls[c-1][d-1]
    for z, x, y in cand:
        ans += z*ls[x][y]
    print(ans)
