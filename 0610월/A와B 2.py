# https://www.acmicpc.net/problem/12919

S = input()
T = input()

s=t=0
for i in S:
    if i == 'B':
        s+=1
for j in T:
    if j == 'B':
        t+= 1    

b_num = t-s

idx = len(S)
prev= [(0,S)]
while idx<len(T):
    next=[]
    for b,i in prev:
        if b+len(T)-idx<b_num:
            continue
        elif b>=b_num:
            next.append((b,i+'A'))
        elif b+len(T)-idx == b_num:
            next.append((b+1,'B'+i[::-1]))
        elif b+len(T)-idx > b_num:
            next.append((b,i+'A'))
            next.append((b+1,'B'+i[::-1]))
    # print(next)
    prev= next
    idx+=1
for _, i in prev:
    if T == i:
        print(1)
        break
else:
    print(0)
