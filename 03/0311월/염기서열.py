# https://softeer.ai/practice/6249

# 4 5
# a..tt
# a.g.t
# gc...
# .c.ag
from itertools import combinations, combinations_with_replacement
N, M = map(int, input().split())
ls = [input() for i in range(N)]

while True:
    print(ls)
    temp = set()
    done = set()
    for a, b in combinations(ls, 2):
        word = ''
        for i in range(M):
            if a[i] == '.':
                word += b[i]
            elif b[i] == '.':
                word += a[i]
            elif a[i] == b[i]:
                word += a[i]
            else:
                temp.add(a)
                temp.add(b)
                break
        else:
            temp.add(word)
            done.add(a)
            done.add(b)
    temp = temp-done
    temp = list(temp)
    if temp == ls:
        break
    else:
        ls = temp

print(temp)
if temp:
    print(len(temp))
else:
    print(1)
