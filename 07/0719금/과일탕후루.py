# https://www.acmicpc.net/problem/30804
from collections import Counter
N = int(input())

ls = list(map(int, input().split()))

cnt = [[0]*(N+1) for _ in range(N+1)]

temp = [0]*10
for i in ls:
    temp[i] += 1

# c = Counter(ls)
cnt[0][0] = temp


def check(k):
    a = 0
    for i in k:
        if i != 0:
            a += 1
    if a <= 2:
        return True
    return False


ans = 10e9
for r in range(N):
    for c in range(N):
        # front
        f, b = ls[r], ls[N-1-c]
        temp = cnt[r][c][:]
        temp[f] -= 1
        cnt[r+1][c] = temp
        if check(temp):
            ans = min(ans, N-r-c-1)

        # back
        temp = cnt[r][c][:]
        temp[b] -= 1
        cnt[r][c+1] = temp
        if check(temp):
            ans = min(ans, N-r-c-1)

print(*cnt, sep='\n')
print(ans)
