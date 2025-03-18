# https://www.acmicpc.net/problem/1941

from itertools import combinations

ls = [list(input()) for _ in range(5)]

'''
25C7=
480700
'''

cord = [(i, j)for i in range(5) for j in range(5)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check(selected):
    visited = [[1]*5 for _ in range(5)]  # 안 고른 데는 가면 안됨
    snum = 0
    for r, c in selected:
        visited[r][c] = 0
        if ls[r][c] == 'S':
            snum += 1

    if snum < 4:  # 4명이 안되면 컷
        return 0

    r, c = selected[0]
    visited[r][c] = 1
    st = [(r, c)]

    cnt = 1

    while st:  # 델타탐색으로 모두 방문 가능한지(인접한지) 검사
        r, c = st.pop()
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if -1 < nr < 5 and -1 < nc < 5 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                st.append((nr, nc))
    if cnt == 7:
        return 1
    else:
        return 0


ans = 0
for selected in combinations(cord, 7):  # 완탐
    ans += check(selected)
print(ans)
