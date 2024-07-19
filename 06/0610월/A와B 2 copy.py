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
# prev= [(0,S)]
prev = [S]
while idx<len(T):
    next=[]
    for i in prev:
        b=0
        for j in i:
            if j == 'B':
                b+=1
        b-=s
        if b+len(T)-idx<b_num:
            continue
        elif b>=b_num:
            next.append(i+'A')
        elif b+len(T)-idx == b_num:
            next.append('B'+i[::-1])
        elif b+len(T)-idx > b_num:
            next.append(i+'A')
            next.append('B'+i[::-1])
    next = list(set(next))
    # print(next)
    prev= next
    idx+=1
for i in prev:
    if T == i:
        print(1)
        break
else:
    print(0)
