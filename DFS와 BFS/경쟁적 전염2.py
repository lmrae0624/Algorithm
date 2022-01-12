from collections import deque

n, k=map(int,input().split())
graph=[]
virus=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],i,j,0))

s,x,y=map(int,input().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(virus):
    q=deque(virus)

    while q:
        num, x, y, time=q.popleft()

        if time==s:
            break

        for m in range(4):
            nx=x+dx[m]
            ny=y+dy[m]

            if 0>nx or nx>=n or 0>ny or ny>=n:
                continue

            if graph[nx][ny]==0:
                graph[nx][ny]=num
                q.append((graph[nx][ny],x,y,time+1))

virus.sort()
bfs(virus)
print(graph[x-1][y-1])