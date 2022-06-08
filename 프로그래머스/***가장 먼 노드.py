def solution(n, edge):
    from collections import deque
    graph=[[]for _ in range(n+1)]
 
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    visited = [0] * (n+1)
    q=deque([1])
    visited[1]=1
    
    
    while q:
        start=q.popleft()
        for i in graph[start]:
            if visited[i]==0:
                q.append(i)
                visited[i]=visited[start]+1

    return visited.count(max(visited))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))




