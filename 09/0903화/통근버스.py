import bisect
N = int(input())
ls = list(map(int, input().split()))

cnt = 0
for i in range(N-2):
    a = ls[i]
    big = []
    small = []
    for j in range(i+1, N):
        temp = ls[j]
        if temp > a:
            big.append(j)
        elif temp < a:
            small.append(j)
    # print(big)
    # print(small)
    # print()
    smallNum = len(small)
    for b in big:
        idx = bisect.bisect_left(small, b)
        cnt += smallNum-idx
print(cnt)
'''
5
4 2 5 3 1

big=[]
small=[]

'''
