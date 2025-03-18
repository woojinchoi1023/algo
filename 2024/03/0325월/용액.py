# https://www.acmicpc.net/problem/2467

N = int(input())
ls = list(map(int, input().split()))
ls.sort()
s, e = 0, N-1
minv = float('inf')
ans = (0, 0)
while s < e:
    if abs(ls[s]+ls[e]) < minv:
        minv = abs(ls[s]+ls[e])
        ans = (ls[s], ls[e])
    if abs(ls[s+1]+ls[e]) < abs(ls[s]+ls[e-1]):
        s += 1
    else:
        e -= 1
print(*ans)
