# https://www.acmicpc.net/problem/9252
# 95퍼 시간초과
s1 = input()
s2 = input()

if len(s1) < len(s2):
    s1, s2 = s2, s1

dp = [['']*len(s1) for _ in range(len(s2)+1)]
for i in range(1, len(s2)+1):
    for j in range(len(s1)):
        temp = ''
        if s2[i-1] == s1[j]:
            temp += s2[i-1]
        if j > 0:
            # 같으면 왼쪽 위 + temp
            # 다르면 왼쪽 or 위 중 긴것
            if temp:
                dp[i][j] = dp[i-1][j-1] + temp
            else:
                if len(dp[i][j-1]) >= len(dp[i-1][j]):
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        else:
            # 위에꺼 있으면 그대로 갖다 쓰고
            # 없으면 걍 넣기
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = temp
print(*dp, sep='\n')

print(len(dp[-1][-1]))
if dp[-1][-1]:
    print(dp[-1][-1])

# mx = 0
# ans = ''
# for i in range(1, len(s2)+1):
#     if len(dp[i][-1]) > mx:
#         mx = len(dp[i][-1])
#         ans = dp[i][-1]
# print(mx)
# if ans:
#     print(ans)
