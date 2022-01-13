from collections import deque
n, m, k, x=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[1e9]*(n+1)

for  _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q=deque([start])
    distance[start]=0
    
    while q:
        now=q.popleft()

        for i in graph[now]:
            distance[i]=min(distance[i],distance[now]+1)
            q.append(i)

bfs(x)

if k not in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if distance[i]==k:
            print(i)


