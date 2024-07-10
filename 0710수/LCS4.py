# https://www.acmicpc.net/problem/13711
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ls = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if a[i-1] == b[j-1]:
            ls[i][j] = ls[i-1][j-1]+1
        else:
            ls[i][j] = max(ls[i-1][j], ls[i][j-1])
print(*ls, sep='\n')


'''
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
