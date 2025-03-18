# https://www.acmicpc.net/problem/20366
# 시간초과

N = int(input())
ls = list(map(int, input().split()))
ls.sort()
cand = [[0]*N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        cand[i][j] = ls[i]+ls[j]

ans = 10e9
for r in range(N):
    for c in range(N):
        if cand[r][c] == 0:
            continue
        idx = 0
        while c+1 < N:
            if cand[idx][c+1] == 0:
                break
            if idx == r:
                idx += 1
                continue
            ans = min(ans, abs(cand[r][c]-cand[idx][c+1]))
            idx += 1

print(ans)
