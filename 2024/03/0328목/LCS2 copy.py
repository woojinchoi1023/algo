# https://www.acmicpc.net/problem/9252
s1 = input()
s2 = input()

if len(s1) < len(s2):
    s1, s2 = s2, s1

dp = [[0]*len(s1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)+1):
    for j in range(len(s1)):
        temp = ''
        if s2[i-1] == s1[j]:
            temp += s2[i-1]
        if j > 0:
            # 같으면 왼쪽 위 + temp
            # 다르면 왼쪽 or 위 중 긴것
            if temp:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                if dp[i][j-1] >= dp[i-1][j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        else:
            # 위에꺼 있으면 그대로 갖다 쓰고
            # 없으면 걍 넣기
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = len(temp)
print(*dp, sep='\n')

# 틀림
ans = ''
i = len(s2)
j = len(s1)-1
print(s2)
print(s1)
while dp[i][j] != 0:
    print(i, j)
    if s1[j] == s2[i-1]:
        print('add', s1[j])
        ans = s1[j] + ans
        i -= 1
        j -= 1
    else:
        left = -1
        if j > 0:
            left = dp[i][j-1]
        top = -1
        if i > 0:
            top = dp[i-1][j-1]
        if left >= top:
            j -= 1
        else:
            i -= 1

print(len(ans))
if ans:
    print(ans)
