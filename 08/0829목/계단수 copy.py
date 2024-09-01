# https://www.acmicpc.net/problem/1562

cnt = 0
N = 1
while N < 41:

    dp = {i: {j: 0 for j in range(1024)} for i in range(10)}

    n = 1
    for i in range(1, 10):
        dp[i][1 << i] = 1

    while n < N:
        newDp = {i: {j: 0 for j in range(1024)} for i in range(10)}
        for i in range(10):
            if i == 0:
                nextnums = [i+1]
            elif i == 9:
                nextnums = [i-1]
            else:
                nextnums = [i-1, i+1]
            for j in range(1024):
                curr = dp[i][j]
                for nextnum in nextnums:
                    nextbin = 1 << nextnum
                    newnum = j | nextbin
                    newDp[nextnum][newnum] += curr
        dp = newDp
        n += 1

    ans = 0
    for i in range(10):
        ans += dp[i][1023]
    print(N, ans % 1000000000)
    cnt += ans
    N += 1
print(cnt)


'''

#1
0 1 2 3 4 5 6 7 8 9

0000000000 -> 10개
1000000000
1: 0100000000
2: 0010000000
3: 0001000000
2,4,8,16,32,64
128,256,512,1024

12: 0110000000
1 :  0100000000 
12 : 0110000000
10 : 1100000000

9876543210
98765432101
89876543210
10123456789

'''
