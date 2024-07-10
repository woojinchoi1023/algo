# https://www.acmicpc.net/problem/13711

import bisect

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = {}
for i in range(N):
    idx.setdefault(a[i], [])
    idx[a[i]].append(i)

arr = []
for i in range(N):
    if idx.get(b[i], []):
        temp = idx[b[i]].pop(0)
        pos = bisect.bisect_left(arr, temp)
        if len(arr) > pos:
            arr[pos] = temp
        else:
            arr.append(temp)
    # print(arr)


print(len(arr))


'''
7
1 1 1 1 2 3 4
1 2 3 4 1 1 1
[0]
[0, 4]
[0, 4, 5]
[0, 4, 5, 6]
[0, 1, 5, 6]
[0, 1, 2, 6]
[0, 1, 2, 3]
4
'''
