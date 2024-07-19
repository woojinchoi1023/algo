# https://softeer.ai/practice/6249

'''
4 5
a..tt
a.g.t
gc...
.c.ag
'''

from itertools import combinations
N, M = map(int, input().split())
ls = [input() for i in range(N)]

d = {}

cand = [i for i in range(N)]
for a, b in combinations(cand, 2):
    tar1, tar2 = ls[a], ls[b]
    word = ''
    for j in range(M):
        if tar1[j] == '.':
            word += tar2[j]
        elif tar2[j] == '.':
            word += tar1[j]
        elif tar1[j] == tar2[j]:
            word += tar1[j]
        else:
            d[(min(a, b), max(a, b))] = 0
            break
    else:
        d[(min(a, b), max(a, b))] = 1

print(d)

# data = [''] * (2**N)

# for i, v in enumerate(combinations_with_replacement(ls, 2)):
#     a, b = v
#     word = ''
#     for j in range(M):
#         if a[j] == '.':
#             word += b[j]
#         elif b[j] == '.':
#             word += a[j]
#         elif a[j] == b[j]:
#             word += a[j]
#         else:
#             data[i] = ''
#             break
#     else:
#         data[i] = word

# print(data)

# ans = [0] * (2**N)


# def dp(idx):

#     return


# for i in range(2**N):
#     if data[i] != '':
#         ans[i] = 1
#     else:
#         ans[i] = dp(i)
