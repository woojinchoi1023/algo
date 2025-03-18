# https://www.acmicpc.net/problem/2473

N = int(input())
ls = list(map(int,input().split()))
ls.sort()
start, mid, end = 0, N//2, N-1
prev = float('inf')
# print(ls)
while True:
    # print(start, mid, end)
    temp = ls[start]+ls[mid]+ls[end]
    if temp==0:
        break
    if temp>0:
        # 중간 -= 1
        # 끝 -=1
        midminus = ls[start]+ls[mid-1]+ls[end]
        endminus = ls[start]+ls[mid]+ls[end-1]
        if abs(midminus) > abs(endminus):
            if abs(temp) > abs(endminus):
                end-=1
            else:
                break
        else:
            if abs(temp) > abs(midminus):
                mid -=1
            else:
                break
    else:
        # 처음 += 1
        # 중간 +=1
        startplus = ls[start+1]+ls[mid]+ls[end]
        midplus = ls[start]+ls[mid+1]+ls[end]
        if abs(midplus) > abs(startplus):
            if abs(temp) > abs(startplus):
                start+=1
            else:
                break
        else:
            if abs(temp) > abs(midplus):
                mid +=1
            else:
                break
if start==mid or mid==end or start==end:
    minv = float('inf')
    idx = 0
    for i in range(N-2):
        s=ls[i]+ls[i+1]+ls[i+2]
        if abs(s)<abs(minv):
            minv = s
            idx = i
    print(ls[idx], ls[idx+1], ls[idx+2])
else:
    print(ls[start],ls[mid],ls[end])

