# https://softeer.ai/practice/6249

# 4 5
# a..tt
# a.g.t
# gc...
# .c.ag
from itertools import combinations
N, M = map(int, input().split())
ls = [input() for i in range(N)]

# comp = combinations([i for i in range(N)], 2)
# diff = set()
# temp = []
# for a, b in comp:
#     for i in range(M):
#         if ls[a][i] == '.' or ls[b][i] == '.':
#             continue
#         if ls[a][i] != ls[b][i]:
#             print(a, b, ls[a][i], ls[b][i])
#             diff.add((a, b))
#             break
#     else:
#         new = ''
#         for i in range(M):
#             if ls[a][i] == '.' and ls[b][i] == '.':
#                 new += '.'
#             elif ls[a][i] != '.':
#                 new += ls[a][i]
#             else:
#                 new += ls[b][i]
#         temp.append(new)

# print(diff)
# print(temp)


def check(ls):
    while True:
        print('ls', ls)
        comp = combinations(ls, 2)
        temp = []
        done = []
        for a, b in comp:
            new = ''
            for i in range(M):
                if a[i] == '.':
                    new += b[i]
                    continue
                if b[i] == '.':
                    new += a[i]
                    continue
                if a[i] != b[i]:
                    break
            else:
                temp.append(new)
                done.append((a, b))
        print(ls)
        for a, b in done:
            ls.remove(a)
            ls.remove(b)
            print(a, b)
        print(ls)
        temp.extend(ls)
        print(temp)
        if ls != temp:
            ls = temp
        else:
            print(temp)
            return


check(ls)
