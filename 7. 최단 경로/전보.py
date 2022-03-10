import heapq
INF=(1e9)
n, m, c=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x, y, z=map(int,input().split())
    graph[x].append((y,z))

def solution(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

solution(c)

count=0
time=0
for i in range(1, n + 1):
    if distance[i] != INF:
        count+=1
        time=max(time,distance[i])

print(count-1, time)





