# https://www.acmicpc.net/problem/6593
from collections import deque


delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    ls = []
    for i in range(L):
        temp = [list(input()) for _ in range(R)]
        ls.append(temp)
        _ = input()

    def findStart(L, R, C):
        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if ls[l][r][c] == 'S':
                        return (l, r, c)

    def findEnd(L, R, C):
        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if ls[l][r][c] == 'E':
                        return (l, r, c)
    S = findStart(L, R, C)
    E = findEnd(L, R, C)

    def bfs(l, r, c):
        v = [[[-1]*C for _ in range(R)]for _ in range(L)]
        v[l][r][c] = 0
        dq = deque()
        dq.append((l, r, c))
        while dq:
            l, r, c = dq.popleft()
            for dl, dr, dc in delta:
                nl, nr, nc = l+dl, r+dr, c+dc
                if -1 < nl < L and -1 < nr < R and -1 < nc < C and ls[nl][nr][nc] != "#" and v[nl][nr][nc] == -1:
                    v[nl][nr][nc] = v[l][r][c]+1
                    if (nl, nr, nc) == E:
                        return v[nl][nr][nc]
                    dq.append((nl, nr, nc))
        return -1
    res = bfs(S[0], S[1], S[2])
    if res != -1:
        print(f'Escaped in {res} minute(s).')
    else:
        print('Trapped!')
