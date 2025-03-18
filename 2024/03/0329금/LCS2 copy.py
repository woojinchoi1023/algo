# https://www.acmicpc.net/problem/9252
s1 = input()
s2 = input()

# if len(s1) < len(s2):
#     s1, s2 = s2, s1

dp = [[0]*len(s1) for _ in range(len(s2))]
#   A C A Y K P
# C 0 1 1 1 1 1
# A 1 1 2 2 2 2
# P 1 1 2 2 2 3
# C 1 2 2 2 2 3
# A 1 2 3 3 3 3
# K 1 2 3 3 4 4

for i in range(len(s2)):
    for j in range(len(s1)):
        temp = ''
        if s2[i] == s1[j]:
            temp += s2[i]
        up = 0
        left = 0
        if i > 0:
            up = dp[i-1][j]
        if j > 0:
            left = dp[i][j-1]
        if temp:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(1, up, left)
        else:
            dp[i][j] = max(up, left)

ans = ''
i,j = len(s2)-1, len(s1)-1
while i>-1 and j>-1 and dp[i][j] != 0:
    if s2[i]==s1[j]:
        ans = s2[i]+ans
        i-=1
        j-=1
    else:
        left = 0
        top = 0
        if i>0:
            top = dp[i-1][j]
        if j>0:
            left = dp[i][j-1]
        if left
    


print(*dp, sep='\n')
