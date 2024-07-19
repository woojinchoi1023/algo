# https://www.acmicpc.net/problem/20366

N = int(input())
ls = list(map(int, input().split()))


ls.sort()
cand = [[0]*N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        cand[i][j] = ls[i]+ls[j]
print(*cand, sep='\n')

ans = 10e9
for i in range(N-1):
    for j in range(i+1, N-1):
        # print(cand[i][j], cand[i+1][j+1])
        ans = min(ans, abs(cand[i][j]-cand[i+1][j+1]))
# print(ans)
# print()

for i in range(N-1):
    for j in range(1, N):
        if cand[i][j] != 0 and cand[i+1][j-1] != 0:
            ans = min(ans, abs(cand[i][j]-cand[i+1][j-1]))
            # print(abs(cand[i][j]-cand[i+1][j-1]))
print(ans)

'''
5
3 5 2 5 9

[0, 5, 7,  7, 11]
[0, 0, 8,  8, 12]
[0, 0, 0, 10, 14]
[0, 0, 0,  0, 14]
[0, 0, 0,  0,  0]

8
1 2 3 4 5 6 7 8
[0, 3, 4, 5, 6,  7,  8,  9]
[0, 0, 5, 6, 7,  8,  9, 10]
[0, 0, 0, 7, 8,  9, 10, 11]
[0, 0, 0, 0, 9, 10, 11, 12]
[0, 0, 0, 0, 0, 11, 12, 13]
[0, 0, 0, 0, 0,  0, 13, 14]
[0, 0, 0, 0, 0,  0,  0, 15]
[0, 0, 0, 0, 0,  0,  0,  0]

8
1 2 3 4 5 6 7 8

3 5 2 5 ...9

8,7 -> 
5,10
8,7

2 3 5 5 9

1,3 : 7,8
2,3 : 7,8
8,14
12,10



'''
