# https://softeer.ai/practice/6249

# 4 5
# a..tt
# a.g.t
# gc...
# .c.ag
from itertools import combinations_with_replacement
N, M = map(int, input().split())
ls = [input() for i in range(N)]

# letters = ['a', 'g', 'c', 't']
# temp = [[]for i in range(M)]
# for i in range(M):
#     for j in range(N):
#         if ls[j][i] != '.' and ls[j][i] not in temp[i]:
#             temp[i].append(ls[j][i])
# print(temp)

# checked = set()

allcase = []


def dfs(idx, res=''):
    if idx > N:
        allcase.append(res)
        return
    cand = []
    for i in range(N):
        for j in range(idx-1):
            if res[j] != ls[i][j]:
                break
        else:
            if res+ls[i][idx] not in cand:
                cand.append(res+ls[i][idx])
    # print(cand)
    for i in cand:
        dfs(idx+1, i)


dfs(0)
print(allcase)
