# https://www.acmicpc.net/problem/2056

import sys
input = sys.stdin.readline

N = int(input())

g = {i: [] for i in range(1, N+1)}  # prev:[next...]
ins = [0]*(N+1)
t = [0]*(N+1)  # time
st = []
for i in range(N):
    dur, cnt, *first = map(int, input().split())
    ins[i+1] = cnt
    t[i+1] = dur
    for j in first:
        g[j].append(i+1)
    if cnt == 0:
        st.append(i+1)

start_time = [0]*(N+1)
ans = 0

while st:
    new_st = []  # 다음에 작업하면 되는 것들
    for i in st:
        end_time = start_time[i]+t[i]  # 끝나는시간
        ans = max(ans, end_time)
        for j in g.get(i, []):  # 다음 작업
            start_time[j] = max(start_time[j], end_time)
            ins[j] -= 1
            if ins[j] == 0:
                new_st.append(j)
    st = new_st
print(ans)

'''
7
5 0
6 1 1
3 1 2
1 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

'''
