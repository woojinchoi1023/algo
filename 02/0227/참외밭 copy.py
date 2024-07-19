# 2477 참외밭

K = int(input())
ls = [list(map(int, input().split()))for _ in range(6)]  # dir, dis

left = [
    (1, 4),
    (4, 2),
    (2, 3),
    (3, 1),
]
for i in range(6):
    start, end = ls[i][0], ls[(i+1) % 6][0]
    if (start, end) not in left:
        # print(i)
        break
x, y = ls[i][1], ls[(i+1) % 6][1]
p = [ls[i][1] for i in range(6) if i % 2 == 0]
q = [ls[i][1] for i in range(6) if i % 2 == 1]
Mx, My = max(p), max(q)

# print(Mx, My, x, y)
print((Mx*My - x*y)*K)
