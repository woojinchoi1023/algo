# https://www.acmicpc.net/problem/2568
import bisect

N = int(input())

ls = []

for _ in range(N):
    x, y = map(int, input().split())
    ls.append((x, y))

ls.sort(key=lambda x: x[0])

lis = []
indices = []
for i in range(N):
    x, y = ls[i]
    idx = bisect.bisect_left(lis, y)
    if idx == len(lis):
        lis.append(y)
    else:
        lis[idx] = y
    indices.append(idx)

ans = []
curr = len(lis)-1
for i in range(N-1, -1, -1):
    if indices[i] == curr:
        curr -= 1
    else:
        ans.append(ls[i][0])

print(N-len(lis))
ans.sort()
for i in ans:
    print(i)

'''
반례
4
1 2
2 3 
3 4
4 1

1
4

LIS [1, 3, 4] 
indices [0, 1, 2, 0]

'''
