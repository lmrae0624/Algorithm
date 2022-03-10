n, m =map(int,input().split())
graph=[]
tmp=[[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

result=0
def solution(wall):
    global result

    if wall==3:
        for i in range(n):
            for j in range(m):
                tmp[i][j]=graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if tmp[i][j]==2:
                    virus_spread(i, j)
        
        result=max(result,safe_count())
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall+=1
                solution(wall)
                graph[i][j]=0
                wall-=1

def virus_spread(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m or tmp[nx][ny]==1:
            continue

        if tmp[nx][ny]==0:
            tmp[nx][ny]=2
            virus_spread(nx,ny)

def safe_count():
    count=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count+=1
    return count

solution(0)
print(result)
        