# https://www.acmicpc.net/problem/9251

s1 = input()
s2 = input()
if len(s1) > len(s2):
    minlen, minv, maxlen, maxv = len(s2), s2, len(s1), s1
else:
    minlen, minv, maxlen, maxv = len(s1), s1, len(s2), s2


dp = {-1: {0: 0}}
for i in range(minlen):
    cand = dp.get(i-1, {})
    # temp = []
    dp.setdefault(i, {})
    dp[i].update(cand)
    for num, idx in cand.items():
        while idx < maxlen-1 and maxv[idx] != minv[i]:
            idx += 1
        if idx < maxlen and maxv[idx] == minv[i] and dp[i].get(num+1, maxlen) > idx:
            dp[i].update({num+1: idx+1})
    # print(dp)
    # print()
print(dp)
print(max(dp[minlen-1].keys()))
