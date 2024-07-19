# https://www.acmicpc.net/problem/9251
# 시간초과
s1 = input()
s2 = input()
if len(s1) > len(s2):
    minlen, minv, maxlen, maxv = len(s2), s2, len(s1), s1
else:
    minlen, minv, maxlen, maxv = len(s1), s1, len(s2), s2


dp = {-1: [(0, 0)]}
mx = 0
for i in range(minlen):
    cand = dp.get(i-1, [])
    temp = []
    for num, idx in cand:
        ori = idx
        temp.append((num, ori))
        while idx < maxlen-1 and maxv[idx] != minv[i]:
            idx += 1
        if maxv[idx] == minv[i]:
            temp.append((num+1, idx))
            if mx < num+1:
                mx = num+1

    dp[i] = temp
    print(dp)
    print()
print(mx)
