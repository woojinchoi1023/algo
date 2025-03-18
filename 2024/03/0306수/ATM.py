# https://www.acmicpc.net/problem/11399

N = int(input())
ls = list(map(int, input().split()))
ls.sort()
for i in range(1, N):
    ls[i] += ls[i-1]
print(sum(ls))
