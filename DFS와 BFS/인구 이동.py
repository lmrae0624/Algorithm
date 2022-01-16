from collections import deque
n, l, r=map(int,input().split())
country=[]
for _ in range(n):
    country.append(list(map(int,input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    q=deque([(i,j)])
    visited[i][j]=True
   
    union=[(i, j)]
    total=country[i][j]
    while q:
        x, y=q.popleft()

        for m in range(4):
            nx=x+dx[m]
            ny=y+dy[m]

            if 0>nx or nx>=n or 0>ny or ny>=n:
                continue
            if visited[nx][ny]:
                continue
            if l <= abs(country[x][y]-country[nx][ny]) <= r:
                union.append((nx,ny))
                q.append((nx,ny))
                total+=country[nx][ny]
                visited[nx][ny]=True
    
    for x, y in union:
        country[x][y]=total//len(union)
    
    return len(union)


result=0
while True:
    visited=[[False]*n for i in range(n)]
    check=False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j) > 1:
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

