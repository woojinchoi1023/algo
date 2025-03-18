# https://softeer.ai/practice/6251
H, K, R = map(int, input().split())

ls = []

for i in range(2**H):
    ls.append(list(map(int, input().split())))

# print(ls)


if H % 2 == 0:
    right = False
else:
    right = True
st = [1]
while True:
    new_st = []
    for i in st:  # 우선자식 먼저 추가
        if right:
            new_st.append(i*2+1)
        else:
            new_st.append(i*2)
    for i in st:  # 나머지 자식
        if right:
            new_st.append(i*2)
        else:
            new_st.append(i*2+1)
    right = not right  # L R 바꾸기
    st = new_st
    if new_st[0] >= 2**H:  # leaf?
        break

order = [i-2**H for i in st]

task = []
for i in zip(*ls):
    for o in order:
        task.append(i[o])

# print(task)

print(sum(task[:R-H]))


'''
3 1 1
8
9
10
11
12
13
14
15

2 1 1
1
2
3
4

'''
