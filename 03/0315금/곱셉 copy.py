# https://www.acmicpc.net/problem/1629


# 시간초과
import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())


def remain(A, B, C):
    sep = B//2
    rem = B-sep
    if sep == 0:
        return A**B % C
    return (remain(A, sep, C) * remain(A, rem, C)) % C


print(remain(A, B, C))
