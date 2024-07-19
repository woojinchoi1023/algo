# https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline
N = int(input().rstrip('\n'))
d = {}
for i in range(N):
    d[i+1] = []
for i in range(N-1):
    a, b = map(int, input().rstrip('\n').split())
    d[a].append(b)
    d[b].append(a)

answer = [0]*(N+1)
visited = [0] * (N+1)
visited[1] = 1


def dfs(s):
    for i in d[s]:
        if not visited[i]:
            visited[i] = 1
            answer[i] = s
            dfs(i)


dfs(1)
for i in range(2, N+1):
    print(answer[i])
