# https://www.acmicpc.net/problem/12919

S = input()
T = input()

prev = [T]
for i in range(len(T)-len(S)):
    next = []
    for j in prev:
        if j[-1]=='A':
            next.append(j[:-1])
        if j[0]=='B':
            j = j[1:]
            j = j[::-1]
            next.append(j)
    # print(next)
    prev=next

for i in prev:
    if S==i:
        print(1)
        break
else:
    print(0)

