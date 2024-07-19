# https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline

M = int(input())
s = set()
for i in range(M):
    a, *b = input().rstrip('\n').split()
    if a == 'add':
        s.add(int(b[0]))
    elif a == 'remove':
        if int(b[0]) in s:
            s.remove(int(b[0]))
    elif a == 'check':
        if int(b[0]) in s:
            print(1)
        else:
            print(0)
    elif a == 'toggle':
        if int(b[0]) in s:
            s.remove(int(b[0]))
        else:
            s.add(int(b[0]))
    elif a == 'all':
        s = set((range(1, 21)))
    else:
        s = set()
