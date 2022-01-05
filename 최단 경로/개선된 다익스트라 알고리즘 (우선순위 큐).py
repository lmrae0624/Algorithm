# 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
import heapq

INF=int(1e9)

n, m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

# graph에 입력 받은 간선 정보 넣기 
for i in range(m):
    a, b, c=map(int,input().split())
    graph[a].append([b,c]) 

def dijkstra(start): 
    h=[]
    heapq.heappush(h,(0,start))
    distance[start]=0

    while h:
        dist, now=heapq.heappop(h)

        #현재 꺼낸 dist가 기존에 저장된 distance[now]보다 크면 이미 처리가 한번된거니까 무시
        if distance[now]<dist: 
            continue

        for i in graph(now):
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]]=cost
                heapq.heappush(h,(cost,i[0]))

dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
