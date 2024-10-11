# https://www.acmicpc.net/problem/1759
L, C = map(int, input().split())
ls = input().split()
ls.sort()
m = {'a', 'e', 'i', 'o', 'u'}

# print(ls)


def dfs(depth=0, pw="", mCnt=0):
    # print(depth, pw)
    if depth > C-1 or len(pw) == L:
        if mCnt > 0 and len(pw) == L and len(pw)-mCnt > 1:
            print(pw)
        return

    isM = True if ls[depth] in m else False
    dfs(depth+1, pw+ls[depth], mCnt+isM)
    dfs(depth+1, pw, mCnt)


dfs()
