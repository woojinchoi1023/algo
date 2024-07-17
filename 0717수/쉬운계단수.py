# https://www.acmicpc.net/problem/10844

'''
3
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[2, 1, 2, 2, 2, 2, 2, 2, 1, 1]
[2, 4, 3, 4, 4, 4, 4, 3, 2, 1]
'''

dt = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8],
}


N = int(input())
dp = [0]+[1]*9
for i in range(N-1):
    newDp = [0]*10
    for j in range(10):
        for k in dt[j]:
            newDp[k] += dp[j]
        newDp[j] %= 1000000000
    dp = newDp

print(sum(dp) % 1000000000)
