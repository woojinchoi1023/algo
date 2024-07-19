T = int(input())
for t in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    # print(ls)
    mx = max(ls)
    d = {
        1: 0,
        2: 0,
    }
    for i in ls:
        d[2] += (mx-i)//2
        d[1] += (mx-i) % 2
    # print(d)
    minv = float('inf')
    for i in range(d[2]+1):
        ones = (d[2]-i)*2 + d[1]
        temp = max(i*2, ones*2-1)
        if minv > temp:
            minv = temp
    print(f'#{t+1}', minv)
    # 1:2
    # 2:1
    # -> 3일
    # 1:0
    # 2:2
    # 1 2 1 로 쪼개면 3일
    # 안쪼개면 4일
    # 2:4
    # 0 2 0 2 0 2 0 2 # 0:4
    # 1 2 1 2 0 2 # 1:3
    # 1 2 1 2 1 0 1
    # 1 2 1 0 1 0 1 0 1 0 1
    # 1 -> 1
    # 2 -> 3
    # 3 -> 10101 =5

'''
1
20
1 3 6 5 5 1 5 4 3 5 4 2 4 6 5 5 4 5 5 3

-> 26
'''
