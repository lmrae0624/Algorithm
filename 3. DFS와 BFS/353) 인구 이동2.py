from collections import deque

n,l,r=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    check=False

    q=deque([(x,y)])
    people=0
    union=[]
    while q:
        a,b=q.popleft()
        people+=graph[a][b]
        union.append((a,b))

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny]:
                continue

            if l<=abs(graph[a][b]-graph[nx][ny])<=r:
                q.append((nx,ny))
                visited[nx][ny]=True
                check=True

    if check:
        people//=len(union)
        for u in union:
            graph[u[0]][u[1]]=people
        visited=[[False]*n for _ in range(n)]

    return check

result=0
while True:
    visited=[[False]*n for i in range(n)]
    check=False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j):
                    check=True
    if not check:
        break
    result+=1

print(result)

# 2 20 50
# 50 30
# 20 40

# 2 40 50
# 50 30
# 20 40

# 2 20 50
# 50 30
# 30 40

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10