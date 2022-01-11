from collections import deque

n, m= map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

move=[(1,0),(-1,0),(0,1),(0,-1)]
visited=[[False]*m for _ in range(n)]

def bfs(x,y):
    q=deque([(x, y)])

    while q:
        x, y=q.popleft()
        visited[x][y]=True

        for i in move:
            nx=x+i[0]
            ny=y+i[1]
            
            if 0>nx or nx>=n or 0>ny or ny>=m or graph[nx][ny]==0 :
                continue
            
            # if graph[nx][ny] == 1: 처음 방문이 아닌 곳은 이미 1보다 크기 때문에 이렇게 확인 가능
            if not visited[nx][ny]:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))
# bfs(0,0)
# print(graph[n-1][m-1])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111