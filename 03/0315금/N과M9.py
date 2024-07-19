# https://www.acmicpc.net/problem/15663

N, M = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

checked = set()


def cal(ans, visited):
    global N, M
    if len(ans) == M:
        temp = ' '.join(str(i) for i in ans)
        if temp not in checked:
            print(temp)
            checked.add(temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ans.append(ls[i])
            cal(ans, visited)
            visited[i] = 0
            ans.pop()


cal([], [0]*N)
