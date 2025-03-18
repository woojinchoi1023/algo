

def solution(edges):
    answer = [0]*4
    # 생성한 정점의 번호, 도넛, 막대, 8자
    g = {}
    in_arrows = {}
    for i in edges:
        a,b = i
        g.setdefault(a,[])
        g.setdefault(b,[])
        in_arrows.setdefault(a,0)
        in_arrows.setdefault(b,0)
        in_arrows[b]+=1
        g[a].append(b)

    print(g)
    print(in_arrows)

    for i in g.keys():
        if len(g[i])>=2 and in_arrows[i]==0:
            answer[0]=i
            break

    print(answer)
    
    

    return answer

edges=[[2, 3], [4, 3], [1, 1], [2, 1]]	
solution(edges)