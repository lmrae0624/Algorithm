INF=int(1e9)
n, m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for i in range(m):
    a, b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x, k= map(int, input().split()) #x=최종방문 지점, k=경유 지점

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
            
distance = graph[1][k] + graph[k][x] #1에서 경유지점 간 거리+경유지점에서 최종지점 간 거리

# 도달할 수 없는 경우, -1을 출력
if distance >= 1e9:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
