# https://www.acmicpc.net/problem/30804
N = int(input())

ls = list(map(int, input().split()))
ans = 0
for i in range(N):
    member = set()
    cnt = 0
    idx = i
    # member.add(ls[idx])
    while len(member) < 3 and idx < N:
        cnt += 1
        member.add(ls[idx])
        print(i, member, cnt)
        idx += 1
    # print(i, cnt)
    ans = max(ans, cnt)
print(ans)
