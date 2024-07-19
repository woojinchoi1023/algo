# https://www.acmicpc.net/problem/18870

N = int(input())
ls = list(map(int, input().split()))
d = {}
for i in ls:
    d.setdefault(i, 0)
temp = list(set(tuple(ls)))
temp.sort()
for i in range(len(temp)):
    d[temp[i]] = i
for i in ls:
    print(d[i], end=' ')
