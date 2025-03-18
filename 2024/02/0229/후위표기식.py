# 1918 후위 표기식

s = input()
st = []
temp = []
ans = ''
for i in s:
    if i.isalpha():
        ans += i
    elif i in '+-/*()':
        if i == '(':
            st.append(i)
        elif i == ')':
            while st[-1] != '(':
                ans += st.pop()
            st.pop()  # del '('
            while st and st[-1] in '*/':
                ans += st.pop()
        elif i in '*/':
            if st and st[-1] in '*/':
                while st and st[-1] in '*/':
                    ans += st.pop()
            st.append(i)
        elif i in '+-':
            if st and st[-1] in '+-':
                while st and st[-1] in '+-':
                    ans += st.pop()
            if st and st[-1] in '*/':
                while st and st[-1] != '(':
                    ans += st.pop()
            st.append(i)

while st:
    ans += st.pop()

print(ans)
