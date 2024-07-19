# https://www.acmicpc.net/problem/1562

'''
10
9876543210

11
8 9876543210
9876543210 1
1 0123456789

8:1,9:1,1:1,
0:1,1:1,9:1,





12
789876543210
989876543210
898765432101
987654321012
987654321010

0:[0,0,0,0,0,0,0,0]
1:
2:

dp[n]=dp[n-1]


'''


def sol(N):
    fdt = {
        0: [1],
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4, 6],
        6: [5, 7],
        7: [6, 8],
        8: [7, 9],
        9: [8],
    }
    bdt = {
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
    fcnt = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    bcnt = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }

    fcnt[9] = 1
    fcnt[8] = 1
    fcnt[1] = 1
    bcnt[0] = 1
    bcnt[1] = 1
    bcnt[9] = 1
    for i in range(12, N+1):
        newfcnt = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
        newbcnt = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
        for j in range(10):
            for k in fdt[j]:
                newfcnt[k] += fcnt[j]
            newfcnt[j] %= 1000000000
            for l in bdt[j]:
                newbcnt[l] += bcnt[j]
            newbcnt[j] %= 1000000000
        # print(sum(newfcnt.values()))
        # print(newbcnt)
        # print()
        fcnt, bcnt = newfcnt, newbcnt
    # print((sum(fcnt.values())) % 1000000000)
    return (sum(fcnt.values())) % 1000000000


# N = int(input())
temp = 0
for t in range(1, 41):
    if t < 10:
        continue
    if t == 10:
        temp += 1
        continue
    temp += sol(t)
print(temp)

# 126461847755
# 7137783642
# 7166190123
# 7166190123

# ans = [0]*101
# ans[10] = 1

# print(ans)
