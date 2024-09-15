# https://www.acmicpc.net/problem/1790
N, K = map(int, input().split())
'''
1..9 1*9
10..99 90*2=180
100..999 = 900*3=2700 ...2889

'''
a = 1  # a자리
temp = 0
while temp+a*(9*10**(a-1)) < K:
    temp += a*(9*10**(a-1))
    a += 1

tar = 10**(a-1)+(K-temp-1)//a
if tar > N:
    print(-1)
    exit()
tar = str(tar)
print(tar[(K-temp-1) % a])
