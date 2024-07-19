# https://www.acmicpc.net/problem/10942
import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
ls = list(map(int, input().rstrip('\n').split()))
M = int(input().rstrip('\n'))

ans = [
    [0]*N for _ in range(N)
]


def check(s, e):
    if s == e or ls[s] == ls[e]:
        return True
    else:
        return False


start = 0

while start < N:
    new_start = start
    end = start
    while new_start > -1 and end < N:
        if new_start == end or ls[new_start] == ls[end]:
            ans[end][new_start] = 1
            new_start -= 1
            end += 1
        else:
            break
    end = start
    new_start = start-1
    while new_start > -1 and end < N:
        if ls[new_start] == ls[end]:
            ans[end][new_start] = 1
            new_start -= 1
            end += 1
        else:
            break
    start += 1


# print(*ans, sep='\n')


for _ in range(M):
    s, e = map(int, input().rstrip('\n').split())
    print(ans[e-1][s-1])
