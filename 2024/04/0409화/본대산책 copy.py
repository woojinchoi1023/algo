# https://www.acmicpc.net/problem/12850

# 인접행렬
# 정 전 미 신 한 진 학 형
ls = [
    [0, 1, 1, 0, 0, 0, 0, 0],  # 정
    [1, 0, 1, 1, 0, 0, 0, 0],  # 전
    [1, 1, 0, 1, 1, 0, 0, 0],  # 미
    [0, 1, 1, 0, 1, 1, 0, 0],  # 신
    [0, 0, 1, 1, 0, 1, 0, 1],  # 한
    [0, 0, 0, 1, 1, 0, 1, 0],  # 진
    [0, 0, 0, 0, 0, 1, 0, 1],  # 학
    [0, 0, 0, 0, 1, 0, 1, 0],  # 형
]

temp = [1, 0, 0, 0, 0, 0, 0, 0]

N = int(input())


def product(res):
    new_temp = [0]*8
    for i in range(8):
        for j in range(8):
            new_temp[i] += res[i][j] * temp[j]
    return new_temp


def cal(arr1, arr2):
    new_ls = [[0]*8 for _ in range(8)]
    for k in range(8):
        for i in range(8):
            for j in range(8):
                new_ls[k][i] += arr1[k][j] * arr2[j][i]
            new_ls[k][i] %= 1000000007
    return new_ls


ans = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]

while N:
    if N % 2:
        ans = cal(ans, ls)
    ls = cal(ls, ls)
    N //= 2

print(product(ans)[0])
