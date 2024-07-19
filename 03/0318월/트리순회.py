N = int(input())
g = {}

for i in range(N):
    a, b, c = input().split()
    g[a] = [b, c]


def preorder(node):
    ans.append(node)
    if g[node][0] != '.':
        preorder(g[node][0])
    if g[node][1] != '.':
        preorder(g[node][1])


ans = []
preorder('A')
print(''.join(ans))


def inorder(node):
    if g[node][0] != '.':
        inorder(g[node][0])
    ans.append(node)
    if g[node][1] != '.':
        inorder(g[node][1])


ans = []
inorder('A')
print(''.join(ans))


def postorder(node):
    if g[node][0] != '.':
        postorder(g[node][0])
    if g[node][1] != '.':
        postorder(g[node][1])
    ans.append(node)


ans = []
postorder('A')
print(''.join(ans))
