from collections import deque

n, m, k, x=map(int,input().split())
graph=[[] for _ in range(n+1)]
count=[0]*(n+1)

for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q=deque([start])
    
    while q:
        tmp=q.popleft()
        
        for i in graph[tmp]:
            if count[i]==0:
                count[i]=count[tmp]+1
                q.append(i)


bfs(x)
if k not in count:
    print(-1)
else:
    for i in range(1, n+1):
        if count[i]==k:
            print(i)
            
# 4 4 2 1 
# 1 2
# 1 3
# 2 3
# 2 4