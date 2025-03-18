# https://www.acmicpc.net/problem/1707
# pypy3로 통과
import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    g = {i: [] for i in range(1, V+1)}
    for _ in range(E):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    nodes = [0]*(V+1)
    nodes[1] = 1

    st = [1]
    stop = False
    while True:
        while st:
            curr = st.pop()
            for c in g.get(curr):
                if nodes[c] == 0:
                    st.append(c)
                    nodes[c] = nodes[curr]*(-1)
                elif nodes[c] == nodes[curr]:
                    stop = True
                    break
        if stop:
            break
        for i in range(1, V+1):
            if nodes[i] == 0:
                nodes[i] = 1
                st.append(i)
                break
        else:
            break
    if stop:
        print('NO')
    else:
        print('YES')
