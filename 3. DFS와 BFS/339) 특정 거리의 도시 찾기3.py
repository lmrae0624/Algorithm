from collections import deque
n, m, k, x=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

visited=[-1]*(n+1)
q=deque([x])
visited[x]=0

while q:
    now=q.popleft()

    for i in graph[now]:
        if visited[i]<0:
            q.append(i)
            visited[i]=visited[now]+1

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if visited[i]==k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4        