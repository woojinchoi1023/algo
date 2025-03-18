# https://www.acmicpc.net/problem/13711
import bisect

N = int(input())

bidx = dict()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(N):
    bidx[b[i]] = i

lcs = []

for i in range(N):
    aNum = a[i]
    aIdxInB = bidx[aNum]
    idx = bisect.bisect_left(lcs, aIdxInB)
    if idx == len(lcs):
        lcs.append(aIdxInB)
    else:
        lcs[idx] = aIdxInB

print(len(lcs))


# print(lcs)
# print(aidx, bidx)
