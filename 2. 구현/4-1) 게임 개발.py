n, m= map(int,input().split())
a, b, d=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,0,1,0] #북 동 남 서
dy=[0,1,0,-1]

count=1
turn=0
while True:
    d-=1
    if d==-1:
        d=3

    nx=a+dx[d]
    ny=b+dy[d]

    if graph[nx][ny]==0:
        graph[nx][ny]=graph[a][b]+1
        count+=1
        a,b=nx,ny
        turn=0
        continue
    else:
        turn+=1
    
    if turn==4:
        nx=a-dx[d]
        ny=b-dy[d]
        if graph[nx][ny]==0:
            a,b=nx,ny
            turn=0
        else:
            break

print(count)
