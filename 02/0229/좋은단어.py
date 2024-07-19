# 3986 좋은단어
N = int(input())
cnt = 0
for i in range(N):
    st = []
    a = input()
    for j in a:
        if st:
            if st[-1] == j:
                st.pop()
            else:
                st.append(j)
        else:
            st.append(j)
    if not st:
        cnt += 1
print(cnt)
