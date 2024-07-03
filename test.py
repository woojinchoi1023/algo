# 이 풀이만 성공

from collections import deque
import sys
input = sys.stdin.readline

nr, nc = map(int, input().rstrip().split())
gp = [list(map(int, input().rstrip().split())) for _ in range(nr)]


def find_air_outside():
    q = deque([(0, 0)])
    gp[0][0] = -1
    v = [[0]*nc for _ in range(nr)]
    v[0][0] = 1
    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_r, next_c = cur_r + dr, cur_c + dc
            if next_r in range(nr) and next_c in range(nc) and not v[next_r][next_c] and gp[next_r][next_c] in {-1, 0}:
                q.append((next_r, next_c))
                gp[next_r][next_c] = -1
                v[next_r][next_c] = 1


cheese = 0
for r in range(1, nr-1):
    for c in range(1, nc-1):
        if gp[r][c] == 1:
            cheese += 1


def is_melt(r, c):
    cnt = 0
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if gp[r+dr][c+dc] == -1:
            cnt += 1
    return cnt >= 2


ans = 0
while cheese:
    find_air_outside()
    check = []
    for r in range(1, nr-1):
        for c in range(1, nc-1):
            if gp[r][c] == 1 and is_melt(r, c):
                check.append((r, c))
                cheese -= 1
    for r, c in check:
        gp[r][c] = -1
    ans += 1
print(ans)


# 이 풀이가 3번 풀이보다 빨라보이는데 왜 시간초과인지 모르겠음.

input = sys.stdin.readline

nr, nc = map(int, input().rstrip().split())
gp = [list(map(int, input().rstrip().split())) for _ in range(nr)]


def find_air_outside():
    q = deque([(0, 0)])
    gp[0][0] = -1
    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_r, next_c = cur_r + dr, cur_c + dc
            if next_r in range(nr) and next_c in range(nc) and not gp[next_r][next_c]:
                q.append((next_r, next_c))
                gp[next_r][next_c] = -1


# 치즈 외부에 있는 공간 -1로 세팅
find_air_outside()

cheese = 0
for r in range(1, nr-1):
    for c in range(1, nc-1):
        if gp[r][c] == 1:
            cheese += 1


def is_melt(sr, sc):
    cnt = 0
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        tr, tc = sr+dr, sc+dc
        if gp[tr][tc] == -1:
            cnt += 1
        # 굳이 조건 추가할 필요 없이, temp를 set으로 쓰면 됨.
        elif gp[tr][tc] == 0:
            temp.add((tr, tc))
    return cnt >= 2


ans = 0
while cheese:
    check = set()
    for r in range(1, nr-1):
        for c in range(1, nc-1):
            temp = set()
            if gp[r][c] == 1 and is_melt(r, c):
                check.add((r, c))
                check.update(temp)
                cheese -= 1
    for r, c in check:
        gp[r][c] = -1
    ans += 1
print(ans)
