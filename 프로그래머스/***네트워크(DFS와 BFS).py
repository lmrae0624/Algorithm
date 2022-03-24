# DFS
def solution(n, computers):
    answer=0
    visited=[False]*n

    def DFS(n,computers,start,visited):
        visited[start]=True
        for connect in range(n):
            if start!=connect and computers[start][connect]==1: #자기 자신이 아니면서 연결된 노드 찾기
                if visited[connect]==False:
                    DFS(n, computers, connect, visited)

    for start in range(n):
        if visited[start]==False:
            DFS(n, computers, start, visited)
            answer+=1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


# BFS
def solution(n, computers):
    from collections import deque
    answer = 0
    visited=[False]*n

    def BFS(n ,computers, start, visited):
        queue=deque([start])
        
        while queue:
            start=queue.popleft()
            visited[start]=True

            for connect in range(n):
                if start!=connect and computers[start][connect]==1:
                    if visited[connect]==False:
                        queue.append(connect)

    for start in range(n):
        if visited[start]==False:
            BFS(n, computers, start, visited)
            answer+=1

    return answer