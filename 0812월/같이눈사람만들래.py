# https://www.acmicpc.net/problem/20366

N = int(input())
ls = list(map(int, input().split()))

ls.sort()
# print(ls)


def sol(a, d):
    # print(a, d)
    for i in range(a+1, d):
        for j in range(i, d):
            return abs(ls[a]+ls[d]-ls[i]-ls[j])


a, b, c, d = 0, 1, N-2, N-1
ans = 10e9
for i in range(N-3):
    a = i
    bot = i+3
    top = N-1
    while bot <= top:
        mid = (bot+top)//2
        res = sol(a, mid)
        if res < ans:
            ans = res
            top = mid-1
        else:
            bot = mid+1
print(ans)

'''
a,b,c,d
a+d b+c ?
a+c b+d ?

b+d-a-c ? a+d-b-c (a+d>b+c)
2b ? 2a
b>a
b+d-a-c ? b+c-a-d (a+d<b+c)
2d>2c
d>c

a+d , b+c가 가장 작음

5
3 5 2 5 9
'''
