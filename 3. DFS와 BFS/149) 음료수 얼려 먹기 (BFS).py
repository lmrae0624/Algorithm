from collections import deque
n, m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input())))

count=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            q=deque([(i, j)])  
            
            while q:
                x, y=q.popleft()
                if 0>x or x>=n or 0>y or y>=m or graph[x][y]==1:
                    continue
                
                graph[x][y]=1

                q.append([x,y+1])
                q.append([x,y-1])
                q.append([x+1,y])
                q.append([x-1,y])
            count+=1
print(count)