# https://www.acmicpc.net/problem/5639
d = {}
st = []
root = 0
while True:
    try:
        n = int(input())
        if not root:
            root = n
        d.setdefault(n, [])
        if st:
            if st[-1] > n:  # 부모보다 작으면
                d[st[-1]].append(n)
                st.append(n)
            else:  # 부모보다 크면
                while st and st[-1] < n:
                    p = st.pop()
                if d.get(p) == []:  # 왼쪽자식이 비어있으면
                    d[p] = [0]
                d[p].append(n)
                st.append(n)
        else:
            st.append(n)
    except:
        break
# print('done')
# print(d)

st = []
st.append(root)
while st:
    curr = st[-1]
    if d.get(curr):
        while d.get(curr):
            st.append(d[curr].pop())
    else:
        if curr:
            print(st.pop())
        else:
            st.pop()


# def postorder(root):
#     st.append(root)
#     if d.get(root):
#         for i in d[st[-1]]:
#             postorder(i)  # 자식계속 탐색
#         print(root)
#     else:  # 자식이 없으면
#         if root:  # 0 은 제외
#             print(root)


# postorder(root)
