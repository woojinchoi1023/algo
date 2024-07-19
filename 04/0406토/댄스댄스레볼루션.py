# https://www.acmicpc.net/problem/2342

import sys
input = sys.stdin.readline

ls = list(map(int, input().split()))

d = {
    (1,1):1,
    (2,2):1,
    (3,3):1,
    (4,4):1,
    (0,1):2,
    (0,2):2,
    (0,3):2,
    (0,4):2,
    (1,2):3,
    (1,4):3,
    (2,1):3,
    (2,3):3,
    (3,2):3,
    (3,4):3,
    (4,3):3,
    (4,1):3,
    (1,3):4,
    (2,4):4,
    (3,1):4,
    (4,2):4,
}

#   1 
# 2 0 4
#   3

# 1 2 2 4 0

# n번째 최소 비용은
# n-1번째 위치 중 최소 비용 + 이동 비용이다

dp = {
    (0,0):0
}
for tar in ls[:-1]:
    temp = {}
    for pos,cost in dp.items():
        l,r = pos
        # same
        if l == tar or r == tar:
            temp[(l,r)] = min(temp.get((l,r),float('inf')), cost+1)
            continue
        # move left
        if temp.get((tar,r), float('inf')) > cost + d[(l,tar)]:
            temp[(tar,r)] = cost + d[(l,tar)]
        # move right
        if temp.get((l,tar), float('inf')) > cost + d[(r,tar)]:
            temp[(l,tar)] = cost + d[(r,tar)]
    dp = temp
    # print(dp)
    # print()

print(min(dp.values()))

