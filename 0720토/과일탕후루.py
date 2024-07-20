# https://www.acmicpc.net/problem/30804
N = int(input())

ls = list(map(int, input().split()))


mx = 1
i, j = 0, 1
d = {}
d[ls[i]] = 1
cnt = 1
while i <= j < N:
    # print(i, j)
    a, b = ls[i], ls[j]
    if len(d.keys()) < 2 or d.get(b, 0) != 0:
        d.setdefault(b, 0)
        d[b] += 1
        j += 1
        cnt += 1
    else:
        d[a] -= 1
        if d[a] == 0:
            del d[a]
        i += 1
        cnt -= 1
    mx = max(mx, cnt)
    # print(i, j, mx)
print(mx)
