# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
INF=int(1e9)

n, m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

# graph에 입력 받은 간선 정보 넣기 
for i in range(m):
    a, b, c=map(int,input().split())
    graph[a].append([b,c]) 

# 최단 거리가 짧은 노드 리턴
def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if not visited[i] and distance[i]<min_value:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):   
    distance[start]=0 #start는0
    visited[start]=True 

    for i in graph[start]:
        distance[i[0]]=i[1] #start에서 연결된 노드에 대한 간선 정보 저장
    
    for i in range(n-1): #start를 제외한 나머지 노드에 대해 반복
        now=get_smallest_node()
        visited[now]=True

        for j in graph[now]: 
            cost=distance[now]+j[1]

            if distance[j[0]] > cost: #현재 노드에서 연결된 값이 더 작을 경우
                distance[j[0]]=cost

dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
