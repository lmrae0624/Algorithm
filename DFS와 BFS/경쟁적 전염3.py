from collections import deque

n, k =map(int,input().split())
graph=[]
virus=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    graph.append(tmp)
    for j in range(n):
        if graph[i][j]>0:
            virus.append((graph[i][j],i,j,0))

s, x, y=map(int,input().split())

virus.sort()

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    q=deque(virus)

    while q:
        num, i, j, time=q.popleft()

        if time==s:
            break

        for m in range(4):
            nx=i+dx[m]
            ny=j+dy[m]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=num
                q.append((num,nx,ny,time+1))

bfs()
print(graph[x-1][y-1])