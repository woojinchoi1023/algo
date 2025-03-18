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

stack = [1]  # 시작 노드인 1을 스택에 넣음
while stack:
    node = stack.pop()
    for i in d[node]:
        if not visited[i]:
            visited[i] = 1
            answer[i] = node
            stack.append(i)

for i in range(2, N+1):
    print(answer[i])
