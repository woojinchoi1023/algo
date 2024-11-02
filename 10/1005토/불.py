# https://www.acmicpc.net/problem/5427
from collections import deque

T = int(input())
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    w, h = map(int, input().split())
    ls = [list(input())for _ in range(h)]
    v = [[-1]*w for _ in range(h)]
    dq = deque()
    sr, sc = 0, 0
    for r in range(h):
        for c in range(w):
            if ls[r][c] == '#':
                v[r][c] = 0
            elif ls[r][c] == '@':
                sr, sc = r, c
            elif ls[r][c] == '*':
                v[r][c] = 0
                dq.append((r, c, 0))

    while dq:  # 불 붙는 시간 조사
        r, c, t = dq.popleft()
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if -1 < nr < h and -1 < nc < w and v[nr][nc] == -1:
                v[nr][nc] = t+1
                dq.append((nr, nc, t+1))

    movedq = deque([(sr, sc, 1)])
    ans = 0
    while movedq:
        r, c, t = movedq.popleft()
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if -1 < nr < h and -1 < nc < w:
                if v[nr][nc] > t or v[nr][nc] == -1:  # 불이 없는 경우 대비
                    movedq.append((nr, nc, t+1))
                    v[nr][nc] = 0
            else:
                ans = t
                break
        if ans:
            print(ans)
            break
    else:
        print('IMPOSSIBLE')

'''
1
7 6
###.###
#.#.#.#
#.....#
#..@..#
#.....#
#######

'''
