import bisect
N = int(input())
d = dict()
names = set()
enter, leave = [], []
for _ in range(N):
    name, action = input().split()
    names.add(name)
    if action == 'enter':
        enter.append(name)
    else:
        leave.append(name)

enter.sort()
leave.sort()

ans = []

for i in names:
    enterNum = bisect.bisect_right(enter, i) - bisect.bisect_left(enter, i)
    leaveNum = bisect.bisect_right(leave, i) - bisect.bisect_left(leave, i)
    if enterNum > leaveNum:
        ans.append(i)

ans.sort(reverse=True)
for i in ans:
    print(i)
