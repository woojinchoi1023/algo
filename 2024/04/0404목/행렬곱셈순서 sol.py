# https://www.acmicpc.net/problem/11049
'''
입력
4
5 3
3 2
2 6
6 3
출력
96

입력
4
5 4
4 3
3 2
2 1
출력
38


입력
5
1 10
10 1
1 10
10 1
1 10
정답
31
'''
# GPT 답
import sys
input= sys.stdin.readline
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n+1) for _ in range(n+1)]
    for length in range(2, n+1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                print(q)
                if q < m[i][j]:
                    m[i][j] = q
            print(*m,sep='\n')
            print()
    return m[1][n]

N = int(input())
p = [0] * (N + 1)
for i in range(N):
    p[i], p[i + 1] = map(int, input().split())

print(matrix_chain_order(p))