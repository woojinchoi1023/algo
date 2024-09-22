# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
ls = [int(input())for _ in range(N)]
ls.sort()
# print(ls)

upper = 1000000000
lower = 1
ans = 0

while lower <= upper:
    mid = (lower+upper)//2
    next = 0
    cnt = 0
    for i in ls:
        if i >= next:
            cnt += 1
            next = i+mid
    # print(mid, cnt)
    if cnt >= C:
        lower = mid+1
        ans = max(ans, mid)
    else:
        upper = mid-1

print(ans)

'''
[1, 2, 8, 4, 9]
1, 2, 4, 8, 9 => 
1깔고 그 담은 5
8에깔고... 12 인데?
mx=100000
mn=1
l=3이면
1깔고4깔고9깔고...
l
'''
