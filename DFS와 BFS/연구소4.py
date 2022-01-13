n, m = map(int,input().split())
graph=[]
tmp=[[0]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,1,-1]

result=0
def dfs(wall):
    global result
    if wall==3:
        for i in range(n):
            for j in range(m):
                tmp[i][j]=graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if graph[i][j]==2:
                    virus(i,j)

        result=max(result,d_count())
        return 
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall+=1
                dfs(wall)
                wall-=1
                graph[i][j]=0
    

def virus(x, y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue

        if tmp[nx][ny]==0:
            tmp[nx][ny]=2
            virus(nx, ny)

def d_count():
    score=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                score+=1
    return score

dfs(0)
print(result)