N = int(input())
d = dict()
for _ in range(N):
    name, action = input().split()
    d[name] = action
ans = []
for i in d.keys():
    if d[i] == 'enter':
        ans.append(i)
ans.sort(reverse=True)
for i in ans:
    print(i)
