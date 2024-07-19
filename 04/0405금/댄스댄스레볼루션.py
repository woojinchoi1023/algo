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
dp = {
    (i,j):1e9 for i in range(5) for j in range(5)
}
# init pos
dp[(0,0)]=0
cand = [(0,0)]
minv = 0
for t in range(len(ls)-1):
    tar = ls[t]
    temp = set()
    minv = float('inf')
    for i,j in cand:
        # move left
        if tar!=j:
            if i==tar:
                dp[(tar,j)] = min(dp[(tar,j)]+1, dp[(i,j)]+d[(i,tar)])
            else:
                dp[(tar,j)] = min(dp[(tar,j)], dp[(i,j)]+d[(i,tar)])
            temp.add((tar,j))
            minv = min(minv, dp[(tar,j)])
            print((i,j), dp[(i,j)],'->',(tar,j),dp[(tar,j)])
        # move right
        if tar!=i:
            if j==tar:
                dp[(i,tar)] = min(dp[(i,tar)]+1, dp[(i,j)]+d[(j,tar)])
            else:
                dp[(i,tar)] = min(dp[(i,tar)], dp[(i,j)]+d[(j,tar)])
            temp.add((i,tar))
            minv = min(minv, dp[(i,tar)])
            print((i,j),dp[(i,j)],'->',(i,tar),dp[(i,tar)])
    cand=temp
    print()
print(minv)

