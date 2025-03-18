# https://acmicpc.net/problem/15654
N, M = map(int, input().split())

ls = list(map(int, input().split()))
ls.sort()


def cal(ans, visited):
    global N, M
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ans.append(ls[i])
            cal(ans, visited)
            visited[i] = 0
            ans.pop()


cal([], [0]*N)
