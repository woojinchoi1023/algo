# 14899 스타트와 링크
import itertools

N = int(input())
data = [list(map(int, input().split()))for _ in range(N)]

comb = itertools.combinations(range(1, N+1), N//2)
minV = float('inf')
checked = set()
for i in comb:  # i = team 1
    if i in checked:
        continue
    t1 = 0
    t2 = 0
    for a, b in itertools.combinations(i, 2):
        # print(i, a, b)
        t1 += data[a-1][b-1]
        t1 += data[b-1][a-1]
    ls = [j for j in range(1, N+1) if j not in i]  # team 2
    checked.add(tuple(ls))
    for a, b in itertools.combinations(ls, 2):
        t2 += data[a-1][b-1]
        t2 += data[b-1][a-1]
    if abs(t1-t2) < minV:
        minV = abs(t1-t2)

print(minV)
