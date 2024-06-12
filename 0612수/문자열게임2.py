# https://www.acmicpc.net/problem/20437

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    ls = [[]for _ in range(26)]
    for i,v in enumerate(W):
        temp = ord(v)-97
        ls[temp].append(i)
    # print(ls)
    ans = []
    for i in ls:
        if len(i)<K:
            continue
        for j in range(0,len(i)-K+1): # sliding window
            ans.append(i[j+K-1]-i[j]+1)
    # print(ans)
    if ans:
        print(min(ans), max(ans))
    else:
        print(-1)

