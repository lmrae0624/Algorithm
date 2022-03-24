def find_parent(parent,x): #루트 노드 찾기
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solution(n, computers):
    parent=[0]*(n)

    for i in range(n): # 부모 테이블에서 부모를 자기 자신으로 설정 
        parent[i]=i

    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                union(parent,i,j)

    # parent로 바로 len을 구하면 단방향 그래프의 경우 오답 처리
    answer = set() # 따라서 computers를 다 탐색한 후 각 노드의 부모를 한번 더 탐색?
    for i in range(n):
        parent[i] = find_parent(parent, i)
        answer.add(parent[i])

    return len(answer)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))