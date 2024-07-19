# https://www.acmicpc.net/problem/9663
# 틀림

N = int(input())
cnt = 0
visited = [[0]*N for _ in range(N)]


def initvisit(i, j):
    global N
    visited = [[0]*N for _ in range(N)]
    cand = [(r, c) for r in range(N) for c in range(
        N) if r == i or c == j or abs(r-i) == abs(c-j)]
    for r, c in cand:
        visited[r][c] = 1
    return visited


def makevisit(i, j, visited):
    global N
    cand = [(r, c) for r in range(N) for c in range(
        N) if r == i or c == j or abs(r-i) == abs(c-j)]
    for r, c in cand:
        visited[r][c] = 1
    return visited


def dfs(depth, visited):
    global cnt
    # print(depth)
    if depth == N:
        cnt += 1
        return
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # print(i, j)
                dfs(depth+1, makevisit(i, j, visited))


temp = [(r, c) for r in range(N) for c in range(
    N) if r == 0 or c == 0 or abs(r) == abs(c)]
for r, c in temp:

    dfs(0, initvisit(r, c))

# for r in range(N):
#     for c in range(N):
#         dfs(0, initvisit(r, c))

print(cnt)
