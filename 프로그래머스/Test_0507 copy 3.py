
def solution(n, paths, gates, summits):
    import heapq
    
    graph=[[]for _ in range(n+1)]
    # 등산로, 이동 시간 저장
    for path in paths:
        graph[path[0]].append((path[1],path[2]))
        graph[path[1]].append((path[0],path[2]))

    def check(start):
        visited=[int(1e9)]*(n+1)
        q=[]
        heapq.heappush(q,(0,start))

        while q:
            cost, now = heapq.heappop(q)
            
            if visited[now] < cost: 
                continue

            for next, dist in graph[now]:
                if next in gates:
                    continue

                tmp=max(cost,dist)
                if visited[next]>tmp:
                    visited[next]=tmp
                    
                    if next not in summits:
                        heapq.heappush(q,(tmp,next)) 

        result=[0,int(1e9)]
        for summit in summits:
            if result[1] > visited[summit]:
                result=[summit,visited[summit]]
            
        return result
    
    answer = [0,int(1e9)]
    for gate in gates:
        num, intensity=check(gate)
        
        if answer[1]>intensity:
            answer=[num,intensity]

    return answer

#print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1,3],[5]))
#print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2,3,4]))
#print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[7],[1,5]))
#print(solution(5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2],[5]))
print(solution(5,[[1, 2, 100], [1, 4, 200], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2],[5]))