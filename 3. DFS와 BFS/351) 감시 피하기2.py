n=int(input())
graph=[]
teacher=[]
tmp=[[0]*n for _ in range(n)]

for i in range(n):
    tmp=list(map(str,input().split()))
    graph.append(tmp)
    for j in range(n):
        if graph[i][j]=='T':
            teacher.append((i,j))
