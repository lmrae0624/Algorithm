from collections import deque
import sys
input = sys.stdin.readline
n,m=map(int,input().split())

array = [[] for _ in range(n + 1)]
for _ in range(m):
    x,y= map(int,input().split())
    array[x].append(y)
    array[y].append(x)

def bfs(start):
    q=deque([start])
    graph[start]=True

    while q:
        now=q.popleft()

        for i in array[now]:
            if not graph[i]:
                q.append(i)
                graph[i]=True

graph=[False]*(n+1)

result=0
for i in range(1,n+1):
    if not graph[i]:
        bfs(i)
        result+=1
        
print(result)


