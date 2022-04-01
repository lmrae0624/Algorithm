from collections import deque

n,k=map(int,input().split())

graph=[]
q=deque()
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]>0:
            q.append((graph[i][j],0,i,j))

s,x,y=map(int,input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

while q:
    virus,time,a,b=q.popleft()
    
    if time==s:
        break

    for i in range(4):
        nx=a+dx[i]
        ny=b+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue

        if graph[nx][ny]==0:
            graph[nx][ny]=virus
            q.append((virus,time+1,nx,ny))

print(graph[x-1][y-1])



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

