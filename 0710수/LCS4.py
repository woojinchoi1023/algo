# https://www.acmicpc.net/problem/13711
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# ls = [[0]*(N+1) for _ in range(N+1)]
idx = {}
for i in range(N):
    idx.setdefault(a[i], [])
    idx[a[i]].append(i)

arr = []
for i in range(N):
    if idx.get(b[i], []):
        max(arr)


print(idx)


'''
7
1 1 1 1 2 3 4
1 2 3 4 1 1 1

{1: [0, 1, 2, 3], 2: [4], 3: [5], 4: [6]}
arr
0 4 5 6
0 1 5 6
0 1 2 6
0 1 2 3

  0 1 1 1 1 2 3 4
0 0 0 0 0 0 0 0 0
1 0 1 1 1 1 1 1 1
2 0 1 1 1 1 2 2 2
3 0 1 1 1 1 2 3 3
4 0
1 0
1 0
1 0

-> 1, 3, 4
-> 1, 2, 4

1 2

'''
