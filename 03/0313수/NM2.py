# https://www.acmicpc.net/problem/15650
N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

answer_list = []


def ncr(n, ans, r):
    if n == len(nums):
        if len(ans) == r:
            answer_list.append(ans[:])
        return
    ans.append(nums[n])
    ncr(n+1, ans, r)
    ans.pop()
    ncr(n+1, ans, r)


ncr(0, [], M)
for i in answer_list:
    print(*i)
