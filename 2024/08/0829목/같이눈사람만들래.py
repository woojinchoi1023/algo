# https://www.acmicpc.net/problem/20366

N = int(input())
ls = list(map(int, input().split()))

ls.sort()

minV = float('inf')
noAbs = 0

a, d = 0, N-1


while a < d-2:

    left_move = float('inf')
    b, c = a+2, d-1
    while b < c:
        temp = ls[a] + ls[d] - ls[b] - ls[c]
        left_move = min(left_move, abs(temp))
        if temp > 0:
            b += 1
        else:
            c -= 1

    right_move = float('inf')
    b, c = a+1, d-2
    while b < c:
        temp = ls[a] + ls[d] - ls[b] - ls[c]
        right_move = min(right_move, abs(temp))
        if temp > 0:
            b += 1
        else:
            c -= 1

    minV = min(minV, left_move, right_move)
    if left_move > right_move:
        d -= 1
    else:
        a += 1
    print('next', ls[a], ls[d])
    print(left_move, right_move)

print(minV)

'''

[2, 3, 5, 5, 9]

tc
6
1 6 7 28 28 50
=> 0

12
6 62 70 10 28 73 10 100 67 62 60 47 
ans = 0
[6, 10, 10, 28, 47, 60, 62, 62, 67, 70, 73, 100]


'''


'''
작은 순서 대로
a, b, c, d

a,d // b,c

a,c // b,d 안됨

if a+d > b+c
a+d-b-c ? b+d-a-c
2a ? 2b => a<b
=> a+d-b-c < b+d-a-c (a,d 한 팀)

if a+d < b+c
b+c-a-d ? b+d-a-c
...

'''
