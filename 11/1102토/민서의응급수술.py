# https://www.acmicpc.net/problem/20955
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

g = {i: [] for i in range(1, N+1)}
parents = [i for i in range(N+1)]


def findparent(a):
    if parents[a] != a:
        parents[a] = findparent(parents[a])
    return parents[a]


def union(a, b):
    pa, pb = findparent(a), findparent(b)
    if pa == pb:
        return True
    if pa > pb:
        parents[a] = pb
    else:
        parents[b] = pa
    return False


new_add = 0
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

    if not union(u, v):
        new_add += 1

# parents[u] = min(parents[u], v)
# parents[v] = min(parents[v], u)
print(parents)

# step 1 : 일단 다 연결
# newadd = 0
# for i in range(1, N+1):
#     temp = findparent(i)
#     if temp == 1:
#         continue
#     union(1, i)
#     g[1].append(temp)
#     g[temp].append(1)
#     newadd += 1

# step 2 : 진짜 필요한 엣지 갯수 카운트
visited = [0]*(N+1)
visited[1] = 1
dq = deque()
dq.append(1)
cnt = 0
while dq:
    curr = dq.popleft()
    for c in g[curr]:
        if visited[c] == 0:
            visited[c] = 1
            dq.append(c)
            cnt += 1

# minus = newadd+M-cnt  # 안 쓴 엣지
# print(newadd+minus)
print(new_add, M-cnt)
# print(newadd, minus)

'''
3 3
1 2
2 3
1 3

'''
