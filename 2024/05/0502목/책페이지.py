# https://www.acmicpc.net/problem/1019
from collections import Counter
N = int(input())

# ls = [str(i).split() for i in range(1,N+1)]
ls = []
for i in range(1,N+1):
    ls += list(str(i))
print(ls)
res = Counter(ls)
print(res)

for i in range(10):
    print(res[str(i)], end=' ')