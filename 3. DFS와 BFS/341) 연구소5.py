n, m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(tmp,x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m :
            continue

        if tmp[nx][ny]==0:
            tmp[nx][ny]=2
            dfs(tmp,nx,ny)

result=0

def cnt(tmp): 
    global result 
    count=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count+=1
    
    result=max(result,count)

tmp=[[0]*m for _ in range(n)]
def wall_creat(wall):
    if wall==3:
        for i in range(n):
            for j in range(m):
                tmp[i][j]=graph[i][j]

        for i in range(n):
            for j in range(m):
                if tmp[i][j]==2:
                    dfs(tmp,i,j)
        
        cnt(tmp)
        return 

    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall_creat(wall+1)
                graph[i][j]=0

wall_creat(0)
print(result)


# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2