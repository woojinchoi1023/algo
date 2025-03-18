# https://www.acmicpc.net/problem/11049
'''
입력
4
5 3
3 2
2 6
6 3
출력
96

입력
4
5 4
4 3
3 2
2 1
출력
38


입력
5
1 10
10 1
1 10
10 1
1 10
정답
31
'''
import sys
input= sys.stdin.readline
N = int(input())
ls = []
ls.extend(map(int,input().split()))
for _ in range(N-2):
    _,y = map(int,input().split())
    ls.append(y)
if N>1:
    x,y = map(int,input().split())
    ls.append(y)

turn = 0
ans = 0

# print(ls)
while turn < N-1:
    minv, minidx = float('inf'), 1
    for i in range(1,len(ls)-1):
        temp = ls[i-1]*ls[i]*ls[i+1]
        if minv>temp:
            minv=temp
            minidx=i
            # print(minidx,minv)
        elif minv==temp and ls[minidx]<ls[i]:
            minv=temp
            minidx=i
            # print(minidx,minv)
    ans += minv
    ls.pop(minidx)
    
    turn+=1
print(ans)


