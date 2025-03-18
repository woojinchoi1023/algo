# https://www.acmicpc.net/problem/11053

N = int(input())
ls = list(map(int, input().split()))

mx = 0
prev = -1


def dfs(idx, prev, cnt):
    global mx, N
    if mx > cnt + N-1-idx:
        return
    if idx == N:
        if cnt > mx:
            mx = cnt
        return
    if prev < ls[idx]:
        # in
        dfs(idx+1, ls[idx], cnt+1)
        # out
    dfs(idx+1, prev, cnt)


dfs(0, prev, 0)
print(mx)
