# https://www.acmicpc.net/problem/2473

N = int(input())
ls = list(map(int,input().split()))
ls.sort()
start, mid, end = 0, N//2, N-1
prev = float('inf')
print(ls)
while True:
    # print(start,mid,end)
    # print(ls[start],ls[mid],ls[end])
    temp = ls[start]+ls[mid]+ls[end]
    if temp > 0: # 10, 11, 3
        if abs(temp-ls[mid]-ls[mid-1]) > abs(temp-ls[end]-ls[end-1]):
            end-=1
        elif abs(temp-ls[mid]-ls[mid-1]) < abs(temp-ls[end]-ls[end-1]):
            mid-=1
        else:
            print(temp)
            break
    elif temp < 0 : # -10, +3 , +11
        if  abs(ls[start+1]-ls[start]+temp) < abs(ls[mid+1]-ls[mid]+temp):
            start+=1
        elif abs(ls[start+1]-ls[start]+temp) > abs(ls[mid+1]-ls[mid]+temp):
            mid+=1
        else: # 같은 경우
            print(temp)
            break
    if abs(prev)<=abs(temp):
        print(prev)
        break
    prev = temp
