import heapq
INF=int(1e9)
n ,m= map(int,input().split())
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b))
    graph[b].append((a))

start=1
q=[(0, start)]
distance[start]=0

while q:
    dist, now=heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost=dist+1
        
        if distance[i] > cost:
            distance[i]=cost
            heapq.heappush(q,(cost,i))

print(distance[1:])

maxdist=max(distance[1:])
print(distance.index(maxdist), maxdist, distance.count(maxdist))

#입력 예시
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2