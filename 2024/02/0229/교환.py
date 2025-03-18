# 1039 교환

N, K = input().split()
N = list(N)
K = int(K)

checked = [set() for i in range(K+1)]


def perm(c):
    # print(c)
    num = int(''.join(N))
    # print(num)

    if num in checked[c]:
        return
    checked[c].add(num)

    if c == K:
        # print(*N)
        # print('ans', num)
        checked[c].add(num)
        return

    for i in range(len(N)):
        for j in range(i+1, len(N)):
            if i == 0 and N[j] == '0':
                continue
            N[i], N[j] = N[j], N[i]
            perm(c+1)
            N[i], N[j] = N[j], N[i]


perm(0)
# print(checked)
if checked[K]:
    print(max(checked[K]))
else:
    print(-1)
