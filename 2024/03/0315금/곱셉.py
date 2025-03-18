# https://www.acmicpc.net/problem/1629


A, B, C = map(int, input().split())

ls = []
pattern = []

for i in range(1, B+1):
    temp = (A**i) % C
    if temp in ls:
        if temp in pattern:
            break
        pattern.append(temp)
    ls.append(temp)
# print(ls)
# print(pattern)
s = len(ls)-len(pattern)  # pattern start
if B-s > 0:
    t = (B-s) % len(pattern)
    print(pattern[t-1])
else:
    print(ls[B-1])
