# https://www.acmicpc.net/problem/11049

'''
입력
4
5 4
4 3
3 2
2 1
출력
38

'''


import sys
input= sys.stdin.readline
N = int(input())
ls = []
# ls.extend(map(int,input().split()))
# for _ in range(N-2):
#     _,y = map(int,input().split())
#     ls.append(y)
# if N>1:
#     x,y = map(int,input().split())
#     ls.append(y)
for _ in range(N):
    x,y = map(int,input().split())
    ls.append((x,y))

print(ls)
def cal(arr1, arr2):
    return arr1[0]
    
dp = [[0]*(N)for _ in range(N)]


# for length in range(2,N+1):
#     for i in range(1, N-length+2):
#         j = i + length - 1

# print(*dp,sep='\n')