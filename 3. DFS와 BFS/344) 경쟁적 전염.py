from collections import deque

n, k=map(int,input().split())
graph=[]
virus=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],0,i,j))

s, x, y=map(int,input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(virus):
    q=deque(virus)
     
    while q:
        num, time, x, y=q.popleft()
        if time==s:
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0>nx or nx>=n or 0>ny or ny>=n :
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=num
                q.append((num,time+1,nx,ny))

virus.sort()
bfs(virus)
print(graph[x - 1][y - 1])

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2
