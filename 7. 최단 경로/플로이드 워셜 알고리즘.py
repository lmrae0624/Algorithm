#모든 지점에서 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
INF=int(1e9)

n, m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신은 0으로 초기화
    for j in range(1, n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a, b, c=map(int,input().split())
    graph[a][b]=c


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j]) # i->j 랑 i->k->j랑 비교

for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
    